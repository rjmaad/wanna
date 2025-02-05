import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:wanna_flutter/src/theme/theme_provider.dart';

import 'src/app.dart';

void main() async {
  runApp(ChangeNotifierProvider(
    create:(context) => ThemeProvider(),
    child: NavigationBarApp()));
}
