<!-- Profile Banner: firma animada (se adapta al tema claro/oscuro de GitHub) -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/main/assets/ymid-signature-dark.gif" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/main/assets/ymid-signature-light.gif" />
    <img src="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/main/assets/ymid-signature-light.gif" alt="Ymid — It's me" width="480" />
  </picture>
</p>

<!-- Language switcher -->
<p align="center">
  <a href="https://github.com/YmidOrtega/YmidOrtega/blob/main/README.md">English</a> · <b>Español</b>
</p>

<!-- Typing Intro -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/tagline-es-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/tagline-es.svg" />
    <img src="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/tagline-es.svg" alt="Componentes que cooperan. Sistemas que cobran vida. Diseño y construyo sistemas backend y APIs escalables." />
  </picture>
</p>

<!-- Badges y Enlaces -->
<p align="center">
  <a href="https://www.ymid.me/" target="_blank"><img src="https://img.shields.io/badge/Portfolio-ymid.me-800020?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/ymidortega/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Ymid%20Ortega-800020?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:yortegap7920@proton.me"><img src="https://img.shields.io/badge/Email-yortegap7920%40proton.me-800020?style=for-the-badge&logo=protonmail&logoColor=white"/></a>
</p>

---

### Sobre mí
- 👋 Desarrollador backend desde Colombia. Construyo aplicaciones Java con Spring Boot, virtual threads y bases SQL y NoSQL.
- 🧠 Me gusta entender cómo funcionan las cosas por dentro y hacerlas más eficientes: concurrencia, automatización y sistemas de baja latencia.
- 🌱 Soy ingeniero ambiental de la Universidad EAN. De la ingeniería me llevé que un problema tiene muchas soluciones; de la EAN, a elegir la que se sostiene en el tiempo.
- ☕ Fuera del código: ciencia ficción, bicicleta e inglés.

---

### Proyectos destacados

<table>
  <tr>
    <!-- PROYECTO 1: TitaniumBOE-Sim -->
    <td width="50%" valign="top">
      <h3 align="center">📈 TitaniumBOE-Sim</h3>
      <p align="justify">
        El protocolo binario de órdenes BOE de Cboe, byte a byte (especificación v2.11.90), sobre un matching engine con prioridad precio-tiempo, bots de trading, una REST API y un feed WebSocket — en un solo JAR. Cada sesión TCP corre en su propio virtual thread de Java 21: 500 sesiones concurrentes y un P99 de 2,5–4,1 ms en el ack de órdenes, medido.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
        <img src="https://img.shields.io/badge/Virtual_Threads-005F87?style=flat-square"/>
        <img src="https://img.shields.io/badge/Javalin-333333?style=flat-square"/>
        <img src="https://img.shields.io/badge/RocksDB-FF6C37?style=flat-square"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/TitaniumBOE-Sim"><b>📂 Ver repositorio »</b></a>
      </div>
    </td>
    <!-- PROYECTO 2: Clínica -->
    <td width="50%" valign="top">
      <h3 align="center">🏥 Clínica — Gestión para una IPS</h3>
      <p align="justify">
        Plataforma de microservicios para una IPS colombiana — pacientes, historia clínica, contratación, admisiones y facturación electrónica DIAN con RIPS, más un asistente con IA local que revisa las facturas emitidas. Los eventos viajan por Kafka con outbox de Debezium, y los tokens ES256 se firman en OpenBao y se intercambian por servicio, sin compartir secretos.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
        <img src="https://img.shields.io/badge/Spring_Cloud-6DB33F?style=flat-square&logo=spring&logoColor=white"/>
        <img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white"/>
        <img src="https://img.shields.io/badge/OpenBao-000000?style=flat-square"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/Clinica"><b>📂 Ver repositorio »</b></a>
      </div>
    </td>
  </tr>
  <tr>
    <!-- PROYECTO 3: Rutea -->
    <td width="50%" valign="top">
      <h3 align="center">🚛 Rutea — Rutas de recolección</h3>
      <p align="justify">
        Planifica microrrutas de recolección de residuos para Bogotá (piloto: Suba) sobre un solver CVRP propio, un ALNS escrito en Java 21. En las 43 instancias X de CVRPLIB de hasta 297 clientes, con 60 s cada una, queda en promedio a 0,35 % de las mejores soluciones conocidas; Timefold, en la misma máquina y con el mismo tiempo, queda a 2,01 %.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
        <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=spring&logoColor=white"/>
        <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB"/>
        <img src="https://img.shields.io/badge/MapLibre-396CB2?style=flat-square&logo=maplibre&logoColor=white"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/Rutea"><b>📂 Ver repositorio »</b></a>
      </div>
    </td>
    <!-- PROYECTO 4: Janus -->
    <td width="50%" valign="top">
      <h3 align="center">📱 Janus — Wake-on-LAN Controller</h3>
      <p align="justify">
        App Android nativa para despertar y apagar equipos en la red — Magic Packet (WOL), apagado remoto por SSH y monitoreo con ping ICMP en segundo plano. Se integra con el sistema mediante Quick Settings Tiles, widget de inicio y notificaciones push de cambio de estado.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white"/>
        <img src="https://img.shields.io/badge/Android_SDK-3DDC84?style=flat-square&logo=android&logoColor=white"/>
        <img src="https://img.shields.io/badge/SSH-000000?style=flat-square"/>
        <img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/Janus"><b>📂 Ver repositorio »</b></a>
      </div>
    </td>
  </tr>
</table>

---

### Métricas & Actividad

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/stats-es-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/stats-es.svg" />
    <img src="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/stats-es.svg" alt="Actividad de YmidOrtega en los últimos 12 meses" />
  </picture>
</div>

---

<!-- Snake Game -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/YmidOrtega/YmidOrtega/blob/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/YmidOrtega/YmidOrtega/blob/output/github-snake.svg" />
    <img alt="GitHub Snake" src="https://github.com/YmidOrtega/YmidOrtega/blob/output/github-snake.svg" />
  </picture>
</p>

---

### ¿Hablamos?
- 💼 **Disponibilidad:** Abierto a proyectos freelance, consultas técnicas o simplemente charlar sobre tecnología.
- 🌐 **Sitio Web:** [ymid.me](https://www.ymid.me/)
- 📨 **Contacto:** [yortegap7920@proton.me](mailto:yortegap7920@proton.me)
- 🔗 **LinkedIn:** [linkedin.com/in/ymidortega](https://www.linkedin.com/in/ymidortega/)
