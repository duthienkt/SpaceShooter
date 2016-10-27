PGraphics g;
PImage s;
void setup()
{
  size(600, 600);
  s = loadImage("tran.png");
  g = createGraphics(s.width* 72, s.height);
  float x = 0;
  for (int i = 0;i< 7; ++i)
  {
    pushMatrix();
    x+= s.width;
    translate(x, s.height/2);
    g.image(s, -s.width/2, -s.height/2);
    popMatrix();
  }
  g.save("transform.png");
}

void draw()
{
  background(40, 40, 200);
  pushMatrix();
  translate(200+s.width/2, 200+s.height/2);
  rotate(frameCount/30.0);
  image(s, -s.width/2, -s.height/2);
  popMatrix();
}