PGraphics g;
PImage []ims = new PImage[7];

void setup()
{
  size(1200, 400);
  for (int i = 0; i< 7; ++i)
  ims[i] = loadImage(i+".png");
  g = createGraphics(ims[0].width*7, ims[0].height);
  
  g.beginDraw();
  g.scale(1, -1);
  float x = 0;
  for (int i = 0; i< 7; ++i){
    g.image(ims[i], x, -g.height);
    x+= ims[i].width;
  }
  g.endDraw();
  g.save("boss1.png");
}

void draw()
{
  background(255);
  scale(1, -1);
  image(ims[(frameCount/2)%7], 0, -height);              
}