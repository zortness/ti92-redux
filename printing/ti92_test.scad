$fn=96;

difference() {
    
    // base rectangle
    translate([0,0,0.01])
    linear_extrude(0.6)
    square([202,112]);

    // cut away the edge layer
    linear_extrude(1)
    import("../drawings/ti92-brd.svg");

    // remove screen island
    translate([38.1,56.5,-0.01])
    linear_extrude(1.01)
    square([102,65]);
    
    translate([38.1,51.5,-0.01])
    linear_extrude(1.01)
    square([22.5,6]);
    
    translate([68,50,-0.01])
    linear_extrude(1.01)
    square([52.5,8]);
    
    //#translate([126.5,52.5,-0.01])
    //linear_extrude(1.01)
    //square([13.5,5]);
    
    // remove other little island
    translate([148.1,108.5,-0.01])
    linear_extrude(1.01)
    square([30.5,5]);
    
    // ** OUTER SCREWS **
    // LEFT EDGE
    /*
    #translate([2.5,12.8,-0.01])
    linear_extrude(1.01)
    circle(1.2);
    
    #translate([2.5,54.5,-0.01])
    linear_extrude(1.01)
    circle(1.2);
    
    #translate([2.5,64.1,-0.01])
    linear_extrude(1.01)
    circle(1.2);
    
    #translate([2.5,99.2,-0.01])
    linear_extrude(1.01)
    circle(1.2);
    
    // LOWER EDGE
    #translate([59,2,-0.01])
    linear_extrude(1.01)
    circle(1.2);
    
    #translate([100,2,-0.01])
    linear_extrude(1.01)
    circle(1.2);
    
    #translate([155.1,2,-0.01])
    linear_extrude(1.01)
    circle(1.2);
    */
}