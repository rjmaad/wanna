import 'package:flutter/material.dart';


void main() => runApp(const Create());

class Create extends StatelessWidget {
  const Create({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark(),
      home: const CreatePage(),
    );
  }
}

  class CreatePage extends StatefulWidget {
  const CreatePage({super.key});

  @override
  State<CreatePage> createState() => _CreatePageState();
}

class _CreatePageState extends State<CreatePage> {
  @override
  Widget build(BuildContext context) {

    return Text("This is the create page");
  }
}
