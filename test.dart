// import 'dart:convert';
// import 'dart:io';

void main(List<String> args) {
  // String? expense = stdin.readLineSync(encoding: utf8);
  printName("fasika", "fikadu");
  print(counter());
}

void printName(String fname, String lname) {
  print(fname + " " + lname);
}

int count = 0;
Function counter() {
  int closure() {
    count += 1;
    return count;
  }

  return closure;
}
