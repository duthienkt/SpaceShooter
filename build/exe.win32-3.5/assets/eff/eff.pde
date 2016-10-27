PGraphics g;
PImage []ims = new PImage[7];

void setup()
{
  size(1200, 400);
  for (int i = 0; i< 5; ++i)
  ims[i] = loadImage("rocket2_"+i+".png");
  g = createGraphics(ims[0].width*5, ims[0].height);
  
  g.beginDraw();
  //g.scale(1, -1);
  float x = 0;
  for (int i = 0; i< 5; ++i){
    g.image(ims[i], x, 0);
    x+= ims[i].width;
  }
  g.endDraw();
  g.save("item_rocket2.png");
}

void draw()
{
  background(255);
  scale(1, -1);
  image(ims[(frameCount/6)%5], 0, -height);              
}