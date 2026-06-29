precision highp float;
varying vec2 v_texcoord;
uniform sampler2D tex;

void main() {
    vec2 uv = v_texcoord;
    vec4 color = texture2D(tex, uv);

    // Вычисляем яркость пикселя
    float luminance = dot(color.rgb, vec3(0.2126, 0.7152, 0.0722));

    // Настраиваем силу свечения в зависимости от яркости/цвета
    // Если цвет яркий (красный, желтый), bloom_strength будет выше
    float bloom_strength = luminance * 0.35; 
    
    // Берем соседние пиксели для эффекта ореола
    vec4 blur = texture2D(tex, uv + 0.0035) + texture2D(tex, uv - 0.0015) +
                texture2D(tex, uv + vec2(0.0015, 0.0)) + texture2D(tex, uv - vec2(0.0015, 0.0));

    // Добавляем свечение к основному цвету
    color.rgb += blur.rgb * bloom_strength;

    gl_FragColor = color;
}
