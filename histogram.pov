#include "colors.inc"

camera {
    location <10, 5, -20>
    look_at <10, 5, 0>
}

light_source {
    <-5, 5, -10>
    color White
    area_light <1, 0, 0>, <0, 1, 0>, 3, 3
    adaptive 1
    jitter
}

plane {
    <0, 1, 0>, 0
    pigment {color White}
    finish {
        ambient 0.4
        reflection 0.2
    }
}

plane {
    <0, 0, -1>, -4
    pigment {color White}
    finish {ambient 0.6}
}




    box {

        <0, 0, 0>, <1, 0.0, 1>
        translate <0, 0, 0>
        texture {
            pigment {color LightBlue }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }



    box {

        <0, 0, 0>, <1, 2.2667681909315425, 1>
        translate <2, 0, 0>
        texture {
            pigment {color LightSteelBlue }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }



    box {

        <0, 0, 0>, <1, 4.604834104242015, 1>
        translate <4, 0, 0>
        texture {
            pigment {color LimeGreen }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }



    box {

        <0, 0, 0>, <1, 6.888635627600426, 1>
        translate <6, 0, 0>
        texture {
            pigment {color Maroon }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }



    box {

        <0, 0, 0>, <1, 6.965026044434994, 1>
        translate <8, 0, 0>
        texture {
            pigment {color MediumAquamarine }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }



    box {

        <0, 0, 0>, <1, 7.502107534962828, 1>
        translate <10, 0, 0>
        texture {
            pigment {color MediumBlue }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }



    box {

        <0, 0, 0>, <1, 8.723118113428644, 1>
        translate <12, 0, 0>
        texture {
            pigment {color MediumForestGreen }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }



    box {

        <0, 0, 0>, <1, 8.876393383452697, 1>
        translate <14, 0, 0>
        texture {
            pigment {color MediumGoldenrod }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }



    box {

        <0, 0, 0>, <1, 9.80593373069535, 1>
        translate <16, 0, 0>
        texture {
            pigment {color MediumOrchid }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }



    box {

        <0, 0, 0>, <1, 10.0, 1>
        translate <18, 0, 0>
        texture {
            pigment {color MediumSeaGreen }
            finish {
                ambient 0.4
                specular 0.3

            }
            normal {
                bumps
                scale 0.1
                turbulence 0.3
            }
        }
    }

