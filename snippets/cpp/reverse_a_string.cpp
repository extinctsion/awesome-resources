// C++ program to reverse a string using stacks
#include <bits/stdc++.h>
using namespace std;
string reverseString(string s){
    stack<char> st;
    for(char c : s){
        st.push(c);
    }
    string reversed = "";
    while(!st.empty()){
        reversed += st.top();
        st.pop();
    }
    return reversed;
}
int main(){
    string s;
    cout<<"Enter a string: ";
    getline(cin,s);
    cout<<"Reversed string: "<<reverseString(s);
    return 0;
}