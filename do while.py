#include <iostream>
using namespace std;
int x,y,z;
int main(){
x = 7;
do{
    z++;
    y = x;
    do{
        cout<<" *";
        y--;
    }while (y >= z);
    cout<<endl;
    }while(z < x);
}
}