import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:wanna_flutter/src/theme/theme_provider.dart';

void main() => runApp(const Profile());

class Profile extends StatelessWidget {
  const Profile({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark(),
      home: const ProfilePage(),
    );
  }
}

  class ProfilePage extends StatefulWidget {
  const ProfilePage({super.key});

  @override
  State<ProfilePage> createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  @override
  Widget build(BuildContext context) {

    return TextButton(onPressed: Provider.of<ThemeProvider>(context, listen: false).toggleTheme, child: Text('Toggle Theme'));
  }
}
