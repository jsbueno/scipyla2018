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


{% for country in countries %}

    box {

        <0, 0, 0>, <1, {{ country.value }}, 1>
        translate <{{ country.position * 2 }}, 0, 0>
        texture {
            pigment {color {{ country.color }} }
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

{% endfor %}
