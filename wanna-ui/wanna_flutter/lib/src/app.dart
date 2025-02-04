import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:wanna_flutter/src/feed/feed.dart';
import 'package:wanna_flutter/src/profile/profile.dart';
import 'package:wanna_flutter/src/theme/theme_provider.dart';
import 'package:wanna_flutter/src/create/create.dart' as create;

/// Flutter code sample for [NavigationBar].

void main() => runApp(const NavigationBarApp());

class NavigationBarApp extends StatelessWidget {
  const NavigationBarApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: Provider.of<ThemeProvider>(context).themeData,
      home: const NavigationExample(),
    );
  }
}

class NavigationExample extends StatefulWidget {
  const NavigationExample({super.key});

  @override
  State<NavigationExample> createState() => _NavigationExampleState();
}

class _NavigationExampleState extends State<NavigationExample> {
  int currentPageIndex = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: NavigationBar(
        onDestinationSelected: (int index) {
          setState(() {
            currentPageIndex = index;
          });
        },
        selectedIndex: currentPageIndex,
        destinations: const <Widget>[
          NavigationDestination(
            selectedIcon: Icon(Icons.groups),
            icon: Icon(Icons.home_outlined),
            label: 'Feed',
          ),
          NavigationDestination(
            icon: Icon(Icons.add),
            label: 'Add',
          ),
          NavigationDestination(
            icon: Icon(Icons.account_circle),
            label: 'Profile',
          ),
        ],
      ),
      body: <Widget>[
        /// Home page
        Feed(),
        /// Create page (weird format because of other uses of "create", might need rename)
        create.Create(),
        /// Profile page
        Profile(),
      ][currentPageIndex],
    );
  }
}
