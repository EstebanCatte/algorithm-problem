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
        vector<vector<vector<int>>> sinr0;
        vector<vector<int>> status;
        int block;
        int tti;

        //constructor
        User(int id, int num_rbg, int num_bs, int num_tti, int num_frame){
            this->id = id;
            this->num_rbg = id;
            this->num_bs = num_bs;
            this->num_tti = num_tti;
            this->num_frame = num_frame;
            this->sinr0 = vector<vector<vector<int>>>(num_rbg, vector<vector<int>>(num_tti, vector<int>(num_bs, 0)));
            this->status = vector<vector<int>>(num_frame, vector<int>(num_tti, 0));
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
        vector<vector<vector<int>>> interf_factor;
        //constructor
        Basestation(int id, int num_user, int num_rbg){
            this->id = id;
            this->interf_factor = vector<vector<vector<int>>> (num_user, vector<vector<int>>(num_user, vector<int>(num_rbg, 0)));
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
        vector<vector<int>> frames;
        vector<vector<float>> interference;
        vector<vector<vector<vector<float>>>> powers;
        vector<vector<vector<vector<float>>>> sinr;
        
        Solver(vector<User>& users,
               vector<Basestation>& basestations, 
               int num_rbg,
               int num_bs,
               int num_user,
               int num_tti,
               int num_frame,
               vector<vector<int>> &frames,
               vector<vector<vector<vector<float>>>> &sinr,
               vector<vector<float>>& interference
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
            this->sinr = vector<vector<vector<vector<float>>>>(num_user,vector<vector<vector<float>>>(num_bs,vector<vector<float>>(num_tti, vector<float>(num_rbg, 0))));
            this->interference = interference;  
            this->powers = vector<vector<vector<vector<float>>>>(num_user,vector<vector<vector<float>>>(num_bs,vector<vector<float>>(num_tti, vector<float>(num_rbg, 0))));
        }

    bool is_communicating(User user, Basestation bs, int rbg, int tti){
        if (this->powers[user.id][bs.id][tti][rbg] > 0){
            return 1;
        }else{
            return 0;
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

    float compute_sinr(User user, Basestation bs, int tti, int rbg){
        float sinr0 = user.sinr0[rbg][tti][bs.id];
        float power = this->powers[user.id][bs.id][tti][rbg];
        float in_interference = 1.0; //this->compute_in_interference(user, bs, tti, rbg);
        float out_interference = 1.0; //this->compute_out_interference(user, bs, tti, rbg);
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

    

    // def compute_rate(self, frame):
    //     //print("#  ..rate computation..")
    //     W = 192
    //     rate = 0
    //     user = self.users[frame["userid"]]
    //     for tti in range(self.num_tti):
    //         for bs in self.basestations:
    //             for rbg in range(self.num_rbg):
    //                 in_com = self.is_communicating(user, bs, rbg, tti)
    //                 sinr = self.compute_geometric_sinr(user, bs, tti)
    //                 rate += in_com * math.log2(1+sinr)
    //     rate = W*rate
    //     frame["rate"] = rate
};

int main(){
    int id = 0;
    int num_rbg = 1;
    int num_bs = 1;
    int num_tti = 1;
    int num_frame = 1;
    User u(id, num_rbg, num_bs, num_tti, num_frame);
}
