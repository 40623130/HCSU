#define EN 8      //步進馬達使能端
#define X_DIR 5   //X軸 步進馬達方向控制
#define Y_DIR 6   //y軸 步進馬達方向控制
#define YY_DIR 7  //y軸 步進馬達方向控制
#define X_STP 2   //x軸 步進控制
#define Y_STP 3   //y軸 步進控制
#define YY_STP 4  //y軸 步進控制
#define X_LIMIT 9  //x軸 極限開關
#define Y_LIMIT 10  //y軸 極限開關

int X_state = 1;
int Y_state = 1;
int stps = 10;
String str;
