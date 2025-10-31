function factorial(n){
    let result = 1;
    for(i=2;i<=n; i++){
        result *= i;
    }
    return result;
}

// Exapmle
console.log(factorial(5));
