#include <bits/stdc++.h>
#include <algorithm>

using namespace std;


class User{
    public:
        int id;
        int num_rbg;
        int num_bs;
        int num_tti;
        int num_frame;
        vector<vector<vector<int> > > sinr0;
        vector<vector<int> > status;
        int block;
        int tti;

        //constructor
        User(int id, int num_rbg, int num_bs, int num_tti, int num_frame){
            this->id = id;
            this->num_rbg = id;
            this->num_bs = num_bs;
            this->num_tti = num_tti;
            this->num_frame = num_frame;
            this->sinr0 = vector<vector<vector<int> > >(num_rbg, vector<vector<int> >(num_tti, vector<int>(num_bs, 0)));
            this->status = vector<vector<int> >(num_frame, vector<int>(num_tti, 0));
            //vector<vector<vector<int>>> sinr0(num_rbg, vector<vector<int>>(num_tti, vector<int>(num_bs, 0)));
            //vector<vector<int>> status(num_frame, vector<int>(num_tti, 0));
            this->block = 0;
            this->tti = 0;
        }
        //destructor
        ~User() {}
};


class Basestation{
    public:
        int id;
        vector<vector<vector<int> > > interf_factor;
        //constructor
        Basestation(int id, int num_user, int num_rbg){
            this->id = id;
            this->interf_factor = vector<vector<vector<int> > > (num_user, vector<vector<int> >(num_user, vector<int>(num_rbg, 0)));
        }
        //destructor
        ~Basestation() {}       
};


class Solver{

    public:
        int  num_rbg;
        int num_bs;
        int num_user;
        int num_tti;
        int num_frame;
        vector<User> users;
        vector<Basestation> basestations;
        vector<vector<int> > frames;
        vector<vector<float> > interference;
        vector<vector<vector<vector<float> > > > powers;
        vector<vector<vector<vector<float> > > > sinr;
        
        Solver(vector<User>& users,
               vector<Basestation>& basestations, 
               int num_rbg,
               int num_bs,
               int num_user,
               int num_tti,
               int num_frame,
               vector<vector<int> > &frames,
               vector<vector<float> > &sinr0,
               vector<vector<float> >& interference
               )
        {  
            this->users = users;
            this->basestations = basestations;
            this->num_rbg = num_rbg;
            this->num_bs = num_bs;
            this->num_user = num_user;
            this->num_tti = num_tti;
            this->num_frame = num_frame;
            this->frames = frames;

            this->formate_interf(interference);
            this->formate_sinr(sinr0);

            this->sinr = vector<vector<vector<vector<float> > > >(num_user,vector<vector<vector<float> > >(num_bs,vector<vector<float> >(num_tti, vector<float>(num_rbg, 0))));
            this->powers = vector<vector<vector<vector<float> > > >(num_user,vector<vector<vector<float> > >(num_bs,vector<vector<float> >(num_tti, vector<float>(num_rbg, 0))));
        }


    float is_communicating(User user, Basestation bs, int tti, int rbg){
        if (this->powers[user.id][bs.id][tti][rbg] > 0){
            return 1.0;
        }else{
            return 0.0;
        }
    }  


    // Fonction pour obtenir les blocs utilisés par un utilisateur pour une station et un tti donnés
    vector<int> getUsedRBG(User& user, Basestation& bs, int tti){
        vector<float>& line = this->powers[user.id][bs.id][tti];
        vector<int> blocks;
        for (int index = 0; index < line.size(); ++index) {
            if (line[index] > 0) {
                blocks.push_back(index);
            }
        }
        return blocks;
    }

    float compute_in_interference(User user, Basestation bs, int tti, int rbg){
        //#Interference from the same bs for user and interf_user
        //#equation 7 numerator
        float interference = 1.0;
        for (int iue=0; iue<this->num_user; iue++){
            if (user.id != this->users[iue].id){
                float in_communication = this->is_communicating(this->users[iue], bs, tti, rbg);
                float interf_factor = bs.interf_factor[iue][user.id][rbg];
                interference *= exp(interf_factor*in_communication);
            }
        }
        return interference;
    }


    float compute_out_interference(User user, Basestation bs, int tti, int rbg){
        //#Pénalité de colision parce que user et inter_user communique avec la même bs sur le même bloc et tti
        //#Interference from the other bs communicating
        //#equation 7 denominator
        float interference = 0;
        for (int ibs=0; ibs<this->num_bs; ibs++){
            if (bs.id != this->basestations[ibs].id){
                for (int iue=0; iue<this->num_user; iue++){
                    if (user.id != this->users[iue].id){
                        float interf_factor = this->basestations[ibs].interf_factor[iue][user.id][rbg];
                        float sinr0 = user.sinr0[rbg][tti][ibs];
                        float power = this->powers[iue][ibs][tti][rbg];
                        interference += sinr0 * power * exp(-interf_factor);
                    }
                }
            }
        }
        return interference;
    }


    float compute_sinr(User user, Basestation bs, int tti, int rbg){
        float sinr0 = user.sinr0[rbg][tti][bs.id];
        float power = this->powers[user.id][bs.id][tti][rbg];
        float in_interference = this->compute_in_interference(user, bs, tti, rbg);
        float out_interference = this->compute_out_interference(user, bs, tti, rbg);
        float sinr = (sinr0 * power * in_interference) / (1+out_interference);
        this->sinr[user.id][bs.id][tti][rbg] = sinr;
        return sinr;
    }


    float compute_geometric_sinr(User user, Basestation bs, int tti){
        float produit = 1.0;
        vector<int> blocks = this->getUsedRBG(user, bs, tti);
        for(int i=0; i<blocks.size(); i++){
            produit *= this->compute_sinr(user, bs, tti, i);
        }
        return pow(produit, 1.0/(max(1, static_cast<int>(blocks.size()))));
    }


    float compute_rate(vector<int> frame)
    {  
        float W = 192.0;
        float rate = 0;
        float sinr;
        User user = this->users[frame[0]]; //0 for userid
        for(int tti=0; tti<this->num_tti; tti++){
            for(int j=0; j<this->num_bs; j++){
                for(int rbg=0; rbg<this->num_rbg; rbg++){
                    float in_com = this->is_communicating(user, this->basestations[j], tti, rbg);
                    sinr = this->compute_geometric_sinr(user, this->basestations[j], tti);
                    rate += in_com * log2(1+sinr);
                }
            }
        }
        rate = W*rate;
        frame[5] = rate;
        return rate;
    }


    bool check_frame_validity(vector<int> frame){
        cout << "...validity check..." << endl;
        cout << "Frame rate : " << frame[5] << " | frame tbs : " << frame[1] << endl;
        bool res = frame[5] >= frame[1];
        cout << "Check is " << res << endl;
        return frame[5] >= frame[1];
    }


    void formate_sinr(vector<vector<float> > sinr){
        for (int t = 0; t < this->num_tti; ++t) {
            for (int b = 0; b < this->num_bs; ++b) {
                for (int r = 0; r < this->num_rbg; ++r) {
                    for (int i = 0; i < this->num_user; ++i){
                        this->users[i].sinr0[r][t][b] = sinr[r + b*this->num_rbg + t*this->num_bs*this->num_rbg][i];
                    }
                }
            }
        }
    }


    void formate_interf(vector<vector<float> > interference){
        for (int i=0; i < this->num_bs; i++){
            for (int r=0; r<this->num_rbg; r++){
                for (int u=0; u<this->num_user; u++){
                    for (int j=0; j<this->num_user; j++){
                        this->basestations[i].interf_factor[u][j][r] = interference[u + r*num_user + i*num_rbg*num_user][j];
                    }
                }
            }
        }
    }


    void network_status(){
        for (int u=0; u<this->num_user; u++){
            for (int b=0; b<this->num_bs; b++){
                for (int t=0; t<this->num_tti; t++){
                    for (int r=0; r<this->num_rbg; r++){
                        float p = this->powers[this->users[u].id][this->basestations[b].id][t][r];
                        float sinr = this->sinr[this->users[u].id][this->basestations[b].id][t][r];
                        if (p>0){
                            cout << "BS " << b << " sending to UE " << u << " with block " << r << " and tti " << t << endl;
                        cout << "SINR of BS" << b << " sending to UE " << u << " is " << sinr << endl;
                        }
                    }
                }
            }
        }
    }


    struct CompareFunction {
        bool operator()(const vector<int>& a, const vector<int>& b) const {
            return a[1] < b[1];
        }
    };


    void sort_frame(vector<vector<int> > frame){
        sort(frame.begin(), frame.end(), CompareFunction());
    }

};

class Heuristic1: public Solver{

    public:
        vector<vector<vector<float> > > heuristic_matrix;

        Heuristic1(vector<User>& users,
               vector<Basestation>& basestations, 
               int num_rbg,
               int num_bs,
               int num_user,
               int num_tti,
               int num_frame,
               vector<vector<int> > &frames,
               vector<vector<float> >& sinr0,
               vector<vector<float> >& interference
               ) : Solver(users, basestations, num_rbg, num_bs, num_user, num_tti, num_frame, frames, sinr0, interference){
                this->heuristic_matrix = vector<vector<vector<float> > >(num_user, vector<vector<float> >(num_rbg, vector<float>(num_tti, 0)));
               }


    void find_max_heuristic(int user_id, int& rbg_out, int& tti_out){
        float max_value = -1000000000.0;
        for (int rbg=0; rbg<this->num_rbg; rbg++){
            for(int tti=0; tti<this->num_tti; tti++){
                float current_value = this->heuristic_matrix[user_id][rbg][tti];
                if (current_value > max_value){
                    max_value = current_value;
                    rbg_out = rbg;
                    tti_out = tti;
                }
            }
        }
    }


    void compute_heuristic_matrix(){
        //metrix is sum(sinr0)
        for (int u=0; u<this->num_user; u++){
            for (int rbg=0; rbg<this->num_rbg; rbg++){
                for (int tti=0; tti<this->num_tti; tti++){
                    float sum=0;
                    //sum computation
                    for (int bs=0; bs<this->num_bs; bs++){
                        sum+= this->users[u].sinr0[rbg][tti][bs];
                    }
                    this->heuristic_matrix[this->users[u].id][rbg][tti] = sum;
                }
            }
        }
    }


    float find_power(int TBS, User user, int rbg, int tti){
        float W = 192.0;
        //2% de marge sur le tbs;
        float cons = pow(2,((static_cast<float>(TBS)/1.98)/W));
        float lower_sinr = -1000000000.0;
        for (int bs=0; bs<this->num_bs; bs++){
            if (user.sinr0[rbg][tti][bs] < lower_sinr){
                lower_sinr = user.sinr0[rbg][tti][bs];
            }
        }
        float value = (cons * sqrt(1/(pow(lower_sinr,2))) * lower_sinr - 1) / lower_sinr;
        return value;
    }


    void print_results(){
        for (int t = 0; t < this->num_tti; ++t) {
            for (int b = 0; b < this->num_bs; ++b) {
                for (int r = 0; r < this->num_rbg; ++r) {
                    for (int i = 0; i < this->num_user; ++i){
                        cout << this->powers[this->users[i].id][this->basestations[b].id][t][r] << " ";
                    }
                    cout << endl;
                }
            }
        }
    }


    void solve(vector<int> frame){
        User user = this->users[frame[2]];
        vector<vector<float> > heuristic = this->heuristic_matrix[user.id];
        int rbg, tti;
        find_max_heuristic(user.id, rbg, tti);
        float score = this->heuristic_matrix[user.id][rbg][tti];
        this->heuristic_matrix[user.id][rbg][tti] = -1000000000;
        float power_to_allocate = this->find_power(frame[1], user, rbg, tti);

        cout << ".....DEBUG SOLVER....." << endl;
        cout << " User " << user.id << " | RBG " << rbg << " | TTI " << tti << " | score : " << score << endl;
        cout << " power allocated " << power_to_allocate << endl;
        power_to_allocate = min(static_cast<float>(this->num_rbg)/static_cast<float>(this->num_bs), power_to_allocate);

        float power_max = 4.0;
        float mini = 0.0;
        for (int bs=0; bs<this->num_bs; bs++){
            mini = std::min(power_to_allocate, power_max);
            this->powers[user.id][this->basestations[bs].id][tti][rbg] = std::max(0.0f, mini);
        }

    } 
};


int main(){

    int num_user, num_bs, num_tti, num_rbg, num_frame;
    cin >> num_user >> num_bs >> num_tti >> num_rbg;
    vector<vector<float> > sinr;

    for (int i = 4; i < 4+num_rbg*num_bs*num_tti; ++i) {
        vector<float> row;
        for (int j = 0; j < num_user; ++j) {
            float value;
            cin >> value;
            row.push_back(value);
        }
        sinr.push_back(row);
    }

    vector<vector<float> > interference;
    for (int i = 4+num_rbg*num_bs*num_tti; i < 4+num_rbg*num_bs*num_tti + num_user*num_rbg*num_bs; ++i) {
        std::vector<float> row;
        for (int j = 0; j < num_user; ++j) {
            float value;
            std::cin >> value;
            row.push_back(value);
        }
        interference.push_back(row);
    }

    cin >> num_frame;
    vector<vector<int> > frames;
    for (int i = 0; i < num_frame; ++i) {
        vector<int> inp;
        for (int j = 0; j < 5; ++j) {
            int value;
            cin >> value;
            inp.push_back(value);
        }
        inp.push_back(0);
        frames.push_back(inp);
    }

    vector<User> users;
    for(int i=0; i<num_user; i++){
        users.push_back(User(i, num_rbg, num_bs, num_tti, num_frame));

    }
    vector<Basestation> basestations;
    for(int i=0; i<num_bs; i++){
        basestations.push_back(Basestation(i, num_user, num_rbg));
    }

    Heuristic1 solver(users, basestations, num_rbg, num_bs, num_user, num_tti, num_frame, frames, sinr, interference);
    solver.sort_frame(frames);
    solver.compute_heuristic_matrix();
    int score = 0;
    for (int i=0; i<num_frame; i++){
        solver.solve(frames[i]);
        solver.compute_rate(frames[i]);
        cout << "Computing frame " << i << " with TBS " << frames[i][1] << " and rate " << frames[i][6] << endl;
        //validity = solver.check_frame_validity(frame)
        //score += validity
        //print("#  Frame {} check: {}".format(i, validity))
    }
    //###########################################
    //                RESULTS")
    //###########################################
    solver.print_results();
}
