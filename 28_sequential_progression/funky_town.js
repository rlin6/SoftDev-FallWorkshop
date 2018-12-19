var studentList = ["ricky", "aaron", "kyle", "kaitlin", "tim", "bo", "damian", "michelle"];

var fib = function(args) {
    if (args == 0) return 0;
    else if (args == 1) return 1;
    else return fib(args - 1) + fib(args - 2);
}

var gcd = function(num, denom) {
    var temp = num % denom;
    if (temp == 0) return denom;
    else return gcd(denom, temp);
}


var randStudent = function() {
    var len = studentList.length;
    var rand = Math.floor(Math.random() * len);
    // console.log(rand);
    return studentList[rand];
}

console.log("fib ------\n\n")
console.log("fib(1): " + fib(1));
console.log("fib(8): " + fib(8));
console.log("fib(4): " + fib(4));
console.log("gcd ------\n\n")
console.log("gcd(8, 10): " + gcd(8, 10));
console.log("gcd(10, 100): " + gcd(10, 100));
console.log("gcd(100, 10): " + gcd(100, 10));
console.log("randomStudent ------\n\n")
console.log(randStudent());
console.log(randStudent());
console.log(randStudent());
console.log(randStudent());
