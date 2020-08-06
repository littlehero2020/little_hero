import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  File _image;
  String _imagepath;
  final picker = ImagePicker();

  @override
  void initState() {
    super.initState();
    loadImage();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Image Picker'),
      ),
      body: Container(
        alignment: Alignment.center,
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              _imagepath != null
                  ? CircleAvatar(
                      backgroundImage: FileImage(File(_imagepath)),
                      radius: 80,
                    )
                  : CircleAvatar(
                      radius: 80,
                      backgroundImage: _image != null
                          ? FileImage(_image)
                          : AssetImage('assets/photos/nophoto.jpg'),
                    ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: RaisedButton(
                  onPressed: () {
                    getImage();
                  },
                  color: Colors.red,
                  child: Text(
                    'Pick image',
                    style:
                        TextStyle(color: Colors.white, fontFamily: 'Lemonada'),
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: RaisedButton(
                  onPressed: () {
                    saveImage(_image.path);
                  },
                  child: Text(
                    'Save',
                    style:
                        TextStyle(color: Colors.white, fontFamily: 'Lemonada'),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future getImage() async {
    final pickedFile = await picker.getImage(source: ImageSource.gallery);
    setState(() {
      _image = File(pickedFile.path);
    });
  }

  void saveImage(path) async {
    SharedPreferences saveimage = await SharedPreferences.getInstance();
    saveimage.setString("imagepath", path);
  }

  void loadImage() async {
    SharedPreferences saveimage = await SharedPreferences.getInstance();
    setState(() {
      _imagepath = saveimage.getString("imagepath");
    });
  }
}
