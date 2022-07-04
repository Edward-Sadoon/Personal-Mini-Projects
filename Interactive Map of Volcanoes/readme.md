# U.S Volcanoes Interactive Map

The purpose of this project is to show the name, elevation, status, and geographical location of each volcano located in the United States on an interactive map.

Using conditional statements, the markers of each volcano is color coded based on the following logic:
```
if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
```

![Screen Shot 2022-07-03 at 9 40 39 PM](https://user-images.githubusercontent.com/71351342/177082726-69430df6-2ef8-4e7c-ab26-45a2754cffbf.png)

When a user clicks on an `i` marker, a popup window would appear containing information about the volcano.

![Screen Shot 2022-07-03 at 9 41 06 PM](https://user-images.githubusercontent.com/71351342/177082736-e677ad6c-1a0a-40a8-a24e-1d0ee0b00d2b.png)
