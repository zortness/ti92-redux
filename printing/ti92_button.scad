$fn=96;



// base (mm)
baseWidth=10.54;
baseHeight=7.16;
baseDepth=2.08;

module baseChunk() {
    // this is naturally a top-right
    linear_extrude(height=baseDepth, scale=0.95)
    square([baseWidth/2,baseHeight/2]);
}

module drawBase() {
    // top right
    baseChunk();
    // top left
    mirror([1,0,0]) baseChunk();
    // bottom right
    mirror([0,1,0]) baseChunk();
    // bottom left
    rotate([0,0,180]) baseChunk();
}

drawBase();

upperWidth=9.22;
upperHeight=5.78;
upperDepth=4.90;

module upperChunk() {
    translate([0,0,baseDepth])
    linear_extrude(height=upperDepth, scale=0.95)
    square([upperWidth/2,upperHeight/2]);
}

module drawUpper() {
    // top right
    upperChunk();
    // top left
    mirror([1,0,0]) upperChunk();
    // bottom right
    mirror([0,1,0]) upperChunk();
    // bottom left
    rotate([0,0,180]) upperChunk();
}

drawUpper();

/*radius=5;
rotate([0,90,0])
translate([-radius,0,0])
linear_extrude(20)
circle(radius);
*/