#include <iostream>
#include <vector>
using namespace std;
void unionFind(int x, int y, vector<int> &parent, vector<int> &rank);
int find(int x, vector<int> &parent);

int main()
{
  int n, m;
  cin >> n >> m;

  int knowFactVal;
  int dap = 0;
  cin >> knowFactVal;

  vector<int> knowFact(knowFactVal);

  for (int i = 0; i < knowFactVal; i++)
  {
    int tmp;
    cin >> tmp;
    knowFact.push_back(tmp);
  }

  vector<int> parent(n + 1);
  for (int i = 1; i <= n; i++)
  {
    parent[i] = i;
  }
  for (int i = 0; i < knowFact.size(); i++)
  {
    parent[knowFact[i]] = 0;
  }
  vector<int> rank(n + 1);
  vector<int> partyParticipants[m];

  for (int i = 0; i < m; i++)
  {
    bool flag = false;
    int partyParticipantCnt;
    cin >> partyParticipantCnt;
    for (int j = 0; j < partyParticipantCnt; j++)
    {
      int a;
      cin >> a;
      partyParticipants[i].push_back(a);
    }

    for (int j = 0; j < partyParticipantCnt - 1; j++)
    {
      unionFind(partyParticipants[i][j], partyParticipants[i][j + 1], parent, rank);
    }
    for (int j = 0; j < partyParticipantCnt; j++)
    {
      for (int k = 0; k < knowFact.size(); k++)
      {
        if (partyParticipants[i][j] == knowFact[k])
        {
          flag = true;
          break;
        }
      }
      if (flag)
      {
        for (int k = 0; k < partyParticipants[i].size(); k++)
        {
          unionFind(partyParticipants[i][k], 0, parent, rank);
        }
        break;
      }
    }
  }
  for (int i = 0; i < m; i++)
  {
    for (int j = 0; j < partyParticipants[i].size(); j++)
    {
      if (find(partyParticipants[i][j], parent) != 0)
      {

        dap++;
        break;
      }
    }
  }
  cout << dap;
}
int find(int x, vector<int> &parent)
{
  if (parent[x] != x)
    parent[x] = find(parent[x], parent);
  return parent[x];
}
void unionFind(int x, int y, vector<int> &parent, vector<int> &rank)
{

  int rootX = find(x, parent);
  int rootY = find(y, parent);

  if (rootX == 0)
  {
    parent[rootY] = 0;
    return;
  }
  if (rootY == 0)
  {
    parent[rootX] = 0;
    return;
  }
  parent[rootX] = rootY;
  return;
}