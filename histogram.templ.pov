#include "colors.inc"

camera {
    location <{{ length / 1.5}} , 8, -{{ length }}>
    look_at <{{ length / 1.5}}, 5, 0>
}

light_source {
    <-5, 5, -15>
    color rgb <1, 1, 1> * 0.8
    area_light <1, 0, 0>, <0, 1, 0>, 3, 3
    adaptive 1
    jitter
}

light_source {
    <10, 15, -15>
    color rgb <1, 1, 1> * 0.3
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
    <0, 0, -1>, -15
    pigment {color White}
    finish {ambient 0.6}
}


{% for country in countries %}
    {% for year in country.years %}
        box {

            <0, 0, 0>, <1, {{ year }}, 1>
            translate <{{ loop.index * 2}}, 0,{{ country.position }}>
            texture {
                pigment {color {{ country.color }} }
                finish {
                    ambient 0.4
                    specular 0.3

                }
                normal {
                    bumps
                    scale 0.2
                    turbulence 0.3
                }
            }
        }
    {% endfor %}
{% endfor %}
