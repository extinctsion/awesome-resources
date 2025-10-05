// C++ program to check if a string is a palindrome using stacks
#include <bits/stdc++.h>
using namespace std;
bool isPalindrome(string s){
    stack<char> st;
    for(int i = 0;i<s.length()/2;i++){
        st.push(s[i]);
    }
    for(int i = (s.length()+1)/2;i<s.length();i++){  //ensure to skip the middle character if length is odd
        if(st.top()!=s[i]){
            return false;
        }
        st.pop();
    }
    return true;
}
int main(){
    string s;
    cout<<"Enter a string: ";
    getline(cin,s);
    if(isPalindrome(s)){
        cout<<"Palindrome";
    }else{
        cout<<"Not a palindrome";
    }
    return 0;
}