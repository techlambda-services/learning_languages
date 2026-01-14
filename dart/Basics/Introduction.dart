//File Import
import 'Functions.dart';
//Import dart:math library for mathematical functions
import 'dart:math';
import 'dart:io';
//Import External Packages

void main()
{
  print('Hello, World!');
  printVariables();
  conditionalStatements();
  sayHello('Alice');
  Person person1 = Person('Bob', 25);
  max(10, 20);
  person1.introduce();
  Person person2 = Person.namedConstructor('Charlie');
  person2.introduce();
print(Color.red);
printWithDelay();

// Instead of the full, explicit syntax:
//VehicleType car = VehicleType.car;
// You can use a dot shorthand:
VehicleType car = .car;
print('Car is fast: ${car.isFast}');
Employee emp = Employee('David', 28, 'TechCorp');
  emp.introduce();
  emp.log('This is a log message.');

}


/*** Variables */
var name = 'Alice';
int age = 30;
double height = 5.7;
bool isStudent = false;




void printVariables() {
  print('Name: $name');
  print('Age: $age');
  print('Height: $height');
  print('Is Student: $isStudent');
}

//Conditional Statements
void conditionalStatements() {
  if (age < 18) {
    print('$name is a minor.');
  } else {
    print('$name is an adult.');
  }

  while (age < 35) {
    print('$name is still young.');
    age += 5;
  }
  for (int i = 0; i < 3; i++) {
    print('Iteration: $i');
  }

  switch (name) {
    case 'Alice':
      print('Hello, Alice!');
      break;
    case 'Bob':
      print('Hello, Bob!');
      break;
    default:
      print('Hello, stranger!');
  }
}
/** Comments */
//Single Line Comment
//Multi-line Comment

/** Class   */

class Person {
  String name;
  int age;

  Person(this.name, this.age);

  Person.namedConstructor(String name) 
      : this.name = name,
        this.age = 0;

  void introduce() {
    print('Hi, I am $name and I am $age years old.');
  }
}

//Enums
enum Color { red, green, blue }

//Enchaned Enums
enum VehicleType {
  car(wheels: 4, seats: 4, maxSpeed: 120),
  bike(wheels: 2, seats: 1, maxSpeed: 80),
  truck(wheels: 6, seats: 2, maxSpeed: 100);

  final int wheels;
  final int seats;
  final int maxSpeed;

  const VehicleType({required this.wheels, required this.seats, required this.maxSpeed});

  bool get isFast => maxSpeed == 100 || maxSpeed > 100;
  
}

//Inheritance
class Employee extends Person with Logger {
  String company;

  Employee(String name, int age, this.company) : super(name, age);

  @override
  void introduce() {
    super.introduce();
    print('I work at $company.');
  }
}
//Mixins
//It's a way to reuse a class's code in multiple class hierarchies.

mixin Logger {
  void log(String message) {
    print('LOG: $message');
  }
}
//Interfaces and Abstract Classes 
/** All Classes in dart implicitly interface  */

class CTO implements Employee {
  @override
  String company;

  @override
  String name;

  @override
  int age;

  CTO(this.name, this.age, this.company);

  @override
  void introduce() {
    print('Hi, I am $name, the CTO of $company.');
  }
  
  @override
  void log(String message) {
    print(message);
  }
} 

abstract class Animal {
  void makeSound();
}

class Dog extends Animal {
  @override
  void makeSound() {
    print('Woof!');
  }
}
class Cat extends Animal {
  @override
  void makeSound() {
    print('Meow!');
  }
}

/** Async Await */
var secondDelay = Duration(seconds: 2);
Future<void> printWithDelay() async {
  await Future.delayed(secondDelay);
  print('Data fetched');
}

//Create Discription
Future<void> creteDiscrete(Iterable<String> objects) async {


  for (final obj in objects) {
    try
    {
      var file = File('data_$obj.txt');
      if(await file.exists())
      {
        var lastModified = await file.lastModified();
        print('Data for $obj already exists. Last modified: $lastModified');
        continue;
      } 
      
      await await file.create();
      await file.writeAsString('Data for $obj');
      
    } on Exception catch (e) {
      print('Error fetching data for $obj: $e');
    }
    
  }
 
}

/*You can also use async*, which gives you a nice, readable way to build streams.*/
Stream<String> report(Person craft, Iterable<String> objects) async* {
  for (final object in objects) {
    await Future.delayed(Duration(seconds: 1));
    yield '${craft.name} flies by $object';
  }
}

//Exception 
// you can use try-catch blocks to handle exceptions gracefully.
//throw exception with throw keyword
// use on or catch or both to catch exceptions
//finally block to execute code regardless of exception occurrence


/** Importent  */
//Null Safety introduced in Dart 2.12
//By default, variables cannot be null unless you explicitly allow it by using the ? operator.
//All Variables are object
//Dart supports Generic Types
//Dart has a rich set of collection types like List, Set, and Map
//Dart don't have public,protected,private access modifiers. Instead, an identifier starting with an underscore (_) is treated as private to its library.
//Dart support top-level functions, meaning you can define functions outside of classes.
//variable tied  to class and functions tied to instances unless marked static
//Dart has a powerful type inference system that can often deduce the type of a variable or expression without explicit type annotations.
//Dart supports both synchronous and asynchronous programming using async, await, and Future keywords.    
//Dart has a built-in package manager called pub, which allows you to manage dependencies and share packages with the Dart community.
//Dart has a comprehensive standard library that provides a wide range of functionalities, from file I/O to networking and more.
//Dart can  report two kind of problems Error and warning 

