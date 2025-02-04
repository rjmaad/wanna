import 'package:flutter/material.dart';

void main() => runApp(const Feed());

class Feed extends StatelessWidget {
  const Feed({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark(),
      home: const FeedPage(),
    );
  }
}

  class FeedPage extends StatefulWidget {
  const FeedPage({super.key});

  @override
  State<FeedPage> createState() => _FeedPageState();
}

class _FeedPageState extends State<FeedPage> {
  @override
  Widget build(BuildContext context) {

    return ListView(
      padding: const EdgeInsets.all(8),
      children: <Widget>[
        Card(
          child: _SampleCard(cardName: 'Wanna 1'),
        ),
        Card(
          child: _SampleCard(cardName: 'Event 1'),
        ),
        Card(
          child: _SampleCard(cardName: 'Wanna 2'),
        ),
      ],
    );
  }
}

class _SampleCard extends StatelessWidget {
  const _SampleCard({required this.cardName});
  final String cardName;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 300,
      height: 100,
      child: Center(child: Text(cardName)),
    );
  }
}