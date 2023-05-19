$fn=96;


/**
* In newer releases of OpenSCAD we'll be able to specify
* layers that we want to import [feature added in 2022]
* import("ti92_back_drawing.svg", id="main_fill")
* id="outline"
* id="hole_casters"
* id="holes"
* But for now, we have each layer as its own file.
*/

height=5;
back_thickness=.6;
tab_thickness=3;

difference() {
    union() {
        translate([0,0,(height-back_thickness)])
        linear_extrude(back_thickness)
        import("../drawings/ti92_back_drawing.svg");
        
        linear_extrude(height)
        import("../drawings/ti92_back_drawing_outline.svg");
        
        linear_extrude(height)
        import("../drawings/ti92_back_drawing_hole_casters.svg");
    }
    
    
    // cut the holes
    translate([0,0,-0.01])
    linear_extrude(height+0.1)
    import("../drawings/ti92_back_drawing_holes.svg");
    
    // cut the USB cable slot
    #translate([54, 79, -0.01])
    linear_extrude(height-back_thickness)
    square([6,18]);
    
    // cut the reset button hole
    #translate([56, 105, 0])
    linear_extrude(height+0.1)
    square([3,5]);
    
    // cut the excess of the tabs
    #translate([43,52.9,tab_thickness])
    linear_extrude(height)
    square([20,5]);
    #translate([44.5,57,tab_thickness])
    linear_extrude(height)
    square([3,3]);
    
    #translate([43,260.8,tab_thickness])
    linear_extrude(height)
    square([20,5]);
    #translate([44.0,259,tab_thickness])
    linear_extrude(height)
    square([3,3]);
    
    // cut some diode interference holes where we took a chunk out for USB plugs on the right side
    #translate([62.5, 240, -0.01])
    linear_extrude(height/2)
    square([5,3]);
    
    #translate([106, 234, -0.01])
    linear_extrude(height/2)
    square([3,5]);
}



