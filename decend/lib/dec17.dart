class Cell {
  int x;
  int y;
  int z;
  int w = 0;

  Cell(this.x, this.y, this.z);

  Cell.fromString(String coords) {
    var nums = coords.substring(1, coords.length - 1).split(',');
    x = int.parse(nums[0].trim());
    y = int.parse(nums[1].trim());
    z = int.parse(nums[2].trim());
  }

  Cell.from4d(this.x, this.y, this.z, this.w);

  Cell.fromString2(String coords) {
    var nums = coords.substring(1, coords.length - 1).split(',');
    x = int.parse(nums[0].trim());
    y = int.parse(nums[1].trim());
    z = int.parse(nums[2].trim());
    w = int.parse(nums[3].trim());
  }

  String toString2() {
    return '(${x}, ${y}, ${z}, ${w})';
  }

  @override
  String toString() {
    return '(${x}, ${y}, ${z})';
  }

  Set<String> neighbours() {
    var neighbours = <String>{};
    for (var dx = -1; dx < 2; ++dx) {
      for (var dy = -1; dy < 2; ++dy) {
        for (var dz = -1; dz < 2; ++dz) {
          neighbours.add(Cell(x + dx, y + dy, z + dz).toString());
        }
      }
    }
    return neighbours;
  }

  Set<String> neighbours2() {
    var neighbours = <String>{};
    for (var dx = -1; dx < 2; ++dx) {
      for (var dy = -1; dy < 2; ++dy) {
        for (var dz = -1; dz < 2; ++dz) {
          for (var dw = -1; dw < 2; ++dw) {
            neighbours
                .add(Cell.from4d(x + dx, y + dy, z + dz, w + dw).toString2());
          }
        }
      }
    }
    return neighbours;
  }

  int activeNeighbours(Set<String> activeCells) {
    var active = 0;
    for (var dx = -1; dx < 2; ++dx) {
      for (var dy = -1; dy < 2; ++dy) {
        for (var dz = -1; dz < 2; ++dz) {
          var different = dx != 0 || dy != 0 || dz != 0;
          var isActive =
              activeCells.contains(Cell(x + dx, y + dy, z + dz).toString());
          if (different && isActive) {
            ++active;
          }
        }
      }
    }
    return active;
  }

  int activeNeighbours2(Set<String> activeCells) {
    var active = 0;
    for (var dx = -1; dx < 2; ++dx) {
      for (var dy = -1; dy < 2; ++dy) {
        for (var dz = -1; dz < 2; ++dz) {
          for (var dw = -1; dw < 2; ++dw) {
            var different = dx != 0 || dy != 0 || dz != 0 || dw != 0;
            var isActive = activeCells.contains(
                Cell.from4d(x + dx, y + dy, z + dz, w + dw).toString2());

            if (different && isActive) {
              ++active;
            }
          }
        }
      }
    }
    return active;
  }
}

Set<String> readInput(String state) {
  var activeCells = <String>{};

  var rows = state.split('\n');
  var z = 0;
  for (var y = 0; y < rows.length; ++y) {
    for (var x = 0; x < rows[y].length; ++x) {
      if (rows[y][x] == '#') {
        activeCells.add(Cell(x, y, z).toString());
      }
    }
  }
  return activeCells;
}

Set<String> readInput2(String state) {
  var activeCells = <String>{};

  var rows = state.split('\n');
  var z = 0;
  var w = 0;
  for (var y = 0; y < rows.length; ++y) {
    for (var x = 0; x < rows[y].length; ++x) {
      if (rows[y][x] == '#') {
        activeCells.add(Cell.from4d(x, y, z, w).toString2());
      }
    }
  }
  return activeCells;
}

int solveFirst(String input) {
  var activeCells = readInput(input);
  var relevantCells = <String>{};
  var survivingCells = <String>{};
  print(activeCells);

  var cycles = 6;

  for (var c = 0; c < cycles; ++c) {
    print('cycle ${c}');
    print('active ${activeCells}');
    for (var cell in activeCells) {
      relevantCells.addAll(Cell.fromString(cell).neighbours());
    }
    print('relevant ${relevantCells}');

    for (var cell in relevantCells) {
      var isActiveCell = activeCells.contains(cell);
      var activeNeighbours =
          Cell.fromString(cell).activeNeighbours(activeCells);
      if (isActiveCell && (activeNeighbours == 2 || activeNeighbours == 3)) {
        survivingCells.add(cell);
      } else if (!isActiveCell && activeNeighbours == 3) {
        survivingCells.add(cell);
      }
    }

    print(activeCells.length);
    print(relevantCells.length);
    print(survivingCells.length);

    activeCells = survivingCells;
    relevantCells.clear();
    survivingCells = <String>{};

    print(activeCells.length);
    print(relevantCells.length);
    print(survivingCells.length);
  }
  return activeCells.length;
}

int solveSecond(String input) {
  var activeCells = readInput2(input);
  var relevantCells = <String>{};
  var survivingCells = <String>{};
  print(activeCells);

  var cycles = 6;

  for (var c = 0; c < cycles; ++c) {
    print('cycle ${c}, active ${activeCells.length}');
    for (var cell in activeCells) {
      relevantCells.addAll(Cell.fromString2(cell).neighbours2());
    }

    for (var cell in relevantCells) {
      var isActiveCell = activeCells.contains(cell);
      var activeNeighbours =
          Cell.fromString2(cell).activeNeighbours2(activeCells);
      if (isActiveCell && (activeNeighbours == 2 || activeNeighbours == 3)) {
        survivingCells.add(cell);
      } else if (!isActiveCell && activeNeighbours == 3) {
        survivingCells.add(cell);
      }
    }

    activeCells = survivingCells;
    relevantCells.clear();
    survivingCells = <String>{};
  }
  return activeCells.length;
}
