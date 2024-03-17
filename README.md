# Estrada de Ferro Garoa


## Modulo `h0`

Funções para converter tamanhos e velocidades entre escala 1:87
e mundo real (**protótipo**)

As funções de tamanho recebem/devolvem medidas em metros.

```python
>>> import h0
>>> h0.from_proto_size(87)  # 87 m
1.0
>>> h0.to_proto_size(.25)  # 25 cm
21.75
>>> h0_cm = 16  # cm
>>> proto_m = h0.to_proto_size(h0_cm / 100)
>>> print(f'A locomotiva U5B H0 de {h0_cm} cm imita um protótipo real de {proto_m} m.')
A locomotiva U5B H0 de 16 cm imita um protótipo real de 13.92 m.

```

As funções de velocidade de H0 para protótipo recebem distância em `m` e tempo em `s`,
e devolvem velocidade em `km/h`. O argumento `s` é opcional, default `1`.

De protótipo para H0, os argumentos são `km` e `h` e os resultados são em `m/s`.
O argumento `h` é opcional, default `1`.

Velocidade de um trem-bala: 313.2 km/s ou 1 m/s na escala H0.

```python
>>> h0.to_proto_speed(1, 1)
313.2
>>> h0.from_proto_speed(313.2, 1)
1.0

```

Velocidade de trem CPTM Frateschi 6318 medida na
[Estrada de Ferro Garoa](https://garoa.net.br/wiki/Estrada_de_Ferro_Garoa)
com 12V na fonte de bancada.

```
>>> d = 4.85  # comprimento da linha externa da EFG
>>> t = 18  # s
>>> vel = h0.to_proto_speed(d, t)
>>> print(f'O trem CPTM Frateschi chega a {d/t:.2f} m/s, ou {vel:.1f} km/h no protótipo real.')
O trem CPTM Frateschi chega a 0.27 m/s, ou 84.4 km/h no protótipo real.

```

Qual deveria ser a velocidade máxima do modelo H0 para imitar os 90 km/h da CPTM?

```
>>> km = 90
>>> ms = h0.from_proto_speed(90)
>>> print(f'Os trens da CPTM chegam a {km} km/h, ou {ms:.2f} m/s na escala H0.')
Os trens da CPTM chegam a 90 km/h, ou 0.29 m/s na escala H0.

```
### Como testar

Execute o script `test.sh`. Ele roda o `doctest` para verificar os exemplos neste arquivo README.md.

