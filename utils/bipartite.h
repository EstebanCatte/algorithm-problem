#ifndef bipartite
#define bipartite

#include "graphs.h"
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
#define INF 2147483647



class BipartiteGraph : public Graph{
public:
    int left_partite_number, right_partite_number;
    
    // Constructor for BipartiteGraph
    BipartiteGraph(int left_partite_number, int right_partite_number, int num_of_node);
    template <class T> static vector<T> hungarian(const std::vector<std::vector<T> > &C);

};

// Constructor definition for BipartiteGraph
BipartiteGraph::BipartiteGraph(int left_partite_number, int right_partite_number, int num_of_node): Graph(num_of_node) {
    this->left_partite_number = left_partite_number;
    this->right_partite_number = right_partite_number;
    for(int l=0; l<left_partite_number; l++){
        for(int r=0; r<right_partite_number; r++){
            graphEdge tempedge;
            tempedge.source = l;
            tempedge.destination = r;
            tempedge.weight = 0;
            this->AddEdge(tempedge);
        }
    }
}


template <class T> 
bool ckmin(T &a, const T &b) { return b < a ? a = b, 1 : 0; }

/**
 * Given J jobs and W workers (J <= W), computes the minimum cost to assign each
 * prefix of jobs to distinct workers.
 *
 * @tparam T a type large enough to represent integers on the order of J *
 * max(|C|)
 * @param C a matrix of dimensions JxW such that C[j][w] = cost to assign j-th
 * job to w-th worker (possibly negative)
 *
 * @return a vector of length J, with the j-th entry equaling the minimum cost
 * to assign the first (j+1) jobs to distinct workers
 */
template <class T>
vector<T> BipartiteGraph::Hungarian(const std::vector<std::vector<T> > &C) 
{
    //const int J = (int)size(C), W = (int)size(C[0]);
    const int J = static_cast<int>(C.size());
    const int W = (J > 0) ? static_cast<int>(C[0].size()) : 0;
    assert(J <= W);
    // job[w] = job assigned to w-th worker, or -1 if no job assigned
    // note: a W-th worker was added for convenience
    vector<int> job(W + 1, -1);
    vector<T> ys(J), yt(W + 1);  // potentials
    // -yt[W] will equal the sum of all deltas
    vector<T> answers;
    const T inf = numeric_limits<T>::max();
    for (int j_cur = 0; j_cur < J; ++j_cur) {  // assign j_cur-th job
        int w_cur = W;
        job[w_cur] = j_cur;
        // min reduced cost over edges from Z to worker w
        vector<T> min_to(W + 1, inf);
        vector<int> prv(W + 1, -1);  // previous worker on alternating path
        vector<bool> in_Z(W + 1);    // whether worker is in Z
        while (job[w_cur] != -1) {   // runs at most j_cur + 1 times
            in_Z[w_cur] = true;
            const int j = job[w_cur];
            T delta = inf;
            int w_next;
            for (int w = 0; w < W; ++w) {
                if (!in_Z[w]) {
                    if (ckmin(min_to[w], C[j][w] - ys[j] - yt[w]))
                        prv[w] = w_cur;
                    if (ckmin(delta, min_to[w])) w_next = w;
                }
            }
            // delta will always be non-negative,
            // except possibly during the first time this loop runs
            // if any entries of C[j_cur] are negative
            for (int w = 0; w <= W; ++w) {
                if (in_Z[w]) ys[job[w]] += delta, yt[w] -= delta;
                else min_to[w] -= delta;
            }
            w_cur = w_next;
        }
        // update assignments along alternating path
        for (int w; w_cur != W; w_cur = w) job[w_cur] = job[w = prv[w_cur]];
        answers.push_back(-yt[W]);
    }
    return answers;
}

#endif 