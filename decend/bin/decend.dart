import 'dart:io';

import 'package:decend/dec17.dart' as dec17;

void main(List<String> arguments) async {
  var input = await File('input.txt').readAsString();
  print('input:\n' + input + '\n');

  // print(dec17.solveFirst(input));
  print(dec17.solveSecond(input));
}
