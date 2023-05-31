#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
    string source = "a.txt";
    ifstream fin(source);
    ofstream fout("b.txt", ios::app);
    if(!fin || !fout) { cerr << source << "열기 오류"; return 0;}
    int count = 0;
    string c;
    while(getline(fin,c)){cout << c << endl;fout << c << endl;count += c.length();}
    cout << "---------------------------" << endl;
    cout << "읽은 바이트 수는" << count << endl;
    fin.close();
    fout.close();
}