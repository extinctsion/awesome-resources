// C++ program to implement binary search
#include <bits/stdc++.h>
using namespace std;
int binarySearch(vector<int>&arr, int target){
    int left = 0, right = arr.size() - 1;
    while(left <= right){
        int mid = left + (right - left) / 2;  // Overflow-safe calculation
        if(arr[mid] == target){
            return mid; // Target found
        }else if(arr[mid] < target){
            left = mid + 1; // Search in the right half
        }else{
            right = mid - 1; // Search in the left half
        }
    }
    return -1; // Target not found
}
int main(){
    int n, target;
    cout<<"Enter number of elements: ";
    cin>>n;
    vector<int> arr(n);
    cout<<"Enter elements: ";
    for(int i = 0;i<n;i++){
        cin>>arr[i];
    }
    sort(arr.begin(), arr.end()); // Ensure the array is sorted
    cout<<"Enter target element: ";
    cin>>target;
    int result = binarySearch(arr, target);
    if(result != -1){
        cout<<"Element found at index: "<<result;
    }else{
        cout<<"Element not found";
    }
    return 0;
}