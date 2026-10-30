<!-- Profile Banner: animated signature (adapts to GitHub's light/dark theme) -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/main/assets/ymid-signature-dark.gif" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/main/assets/ymid-signature-light.gif" />
    <img src="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/main/assets/ymid-signature-light.gif" alt="Ymid — It's me" width="480" />
  </picture>
</p>

<!-- Language switcher -->
<p align="center">
  <b>English</b> · <a href="https://github.com/YmidOrtega/YmidOrtega/blob/main/README.es.md">Español</a>
</p>

<!-- Typing Intro -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/tagline-en-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/tagline-en.svg" />
    <img src="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/tagline-en.svg" alt="Components that cooperate. Systems that come alive. I design and build scalable backend systems and APIs" />
  </picture>
</p>

<!-- Badges & Links -->
<p align="center">
  <a href="https://www.ymid.me/" target="_blank"><img src="https://img.shields.io/badge/Portfolio-ymid.me-800020?style=for-the-badge&logo=google-chrome&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/ymidortega/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Ymid%20Ortega-800020?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:yortegap7920@proton.me"><img src="https://img.shields.io/badge/Email-yortegap7920%40proton.me-800020?style=for-the-badge&logo=protonmail&logoColor=white"/></a>
</p>

---

### About me
- 👋 Backend developer from Colombia. I build Java applications with Spring Boot, virtual threads and SQL/NoSQL databases.
- 🧠 I enjoy understanding how things work under the hood and finding ways to make them more efficient: concurrency, automation and low-latency systems.
- 🌱 I'm an environmental engineer from Universidad EAN. Engineering taught me that a problem has many solutions; EAN taught me to choose the one that lasts.
- ☕ Outside the code: science fiction, cycling and languages.

---

### Featured projects

<table>
  <tr>
    <!-- PROJECT 1: TitaniumBOE-Sim -->
    <td width="50%" valign="top">
      <h3 align="center">📈 TitaniumBOE-Sim</h3>
      <p align="justify">
        Cboe's BOE binary order-entry protocol, byte for byte (spec v2.11.90), behind a price-time matching engine, trading bots, a REST API and a WebSocket feed — one JAR. Each TCP session runs on its own Java 21 virtual thread: 500 concurrent sessions and an order-ack P99 of 2.5–4.1 ms, measured.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
        <img src="https://img.shields.io/badge/Virtual_Threads-005F87?style=flat-square"/>
        <img src="https://img.shields.io/badge/Javalin-333333?style=flat-square"/>
        <img src="https://img.shields.io/badge/RocksDB-FF6C37?style=flat-square"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/TitaniumBOE-Sim"><b>📂 View repository »</b></a>
      </div>
    </td>
    <!-- PROJECT 2: Clínica -->
    <td width="50%" valign="top">
      <h3 align="center">🏥 Clínica — Healthcare Provider Platform</h3>
      <p align="justify">
        Microservices platform for a Colombian healthcare provider — patients, clinical records, contracting, admissions and billing with DIAN e-invoicing and RIPS, plus an assistant on a local LLM that reviews issued invoices. Events flow through Kafka with a Debezium outbox, and ES256 tokens are signed in OpenBao and exchanged per service, with no shared secrets.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
        <img src="https://img.shields.io/badge/Spring_Cloud-6DB33F?style=flat-square&logo=spring&logoColor=white"/>
        <img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white"/>
        <img src="https://img.shields.io/badge/OpenBao-000000?style=flat-square"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/Clinica"><b>📂 View repository »</b></a>
      </div>
    </td>
  </tr>
  <tr>
    <!-- PROJECT 3: Rutea -->
    <td width="50%" valign="top">
      <h3 align="center">🚛 Rutea — Waste Collection Routes</h3>
      <p align="justify">
        Plans waste-collection micro-routes for Bogotá (pilot: Suba) on its own CVRP solver, an ALNS written in Java 21. Across the 43 CVRPLIB X instances of up to 297 customers, with 60 s each, it lands 0.35% from the best-known solutions on average; Timefold, on the same machine and budget, lands 2.01% away.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
        <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=spring&logoColor=white"/>
        <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB"/>
        <img src="https://img.shields.io/badge/MapLibre-396CB2?style=flat-square&logo=maplibre&logoColor=white"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/Rutea"><b>📂 View repository »</b></a>
      </div>
    </td>
    <!-- PROJECT 4: Awaken -->
    <td width="50%" valign="top">
      <h3 align="center">📱 Awaken — Wake-on-LAN Controller</h3>
      <p align="justify">
        Native Android app to wake and shut down devices on the network — Magic Packet (WOL), remote shutdown via SSH and background ICMP ping monitoring. Integrates with the system through Quick Settings Tiles, a home screen widget and push notifications on status change.
      </p>
      <p align="center">
        <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white"/>
        <img src="https://img.shields.io/badge/Android_SDK-3DDC84?style=flat-square&logo=android&logoColor=white"/>
        <img src="https://img.shields.io/badge/SSH-000000?style=flat-square"/>
        <img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black"/>
      </p>
      <div align="center">
        <a href="https://github.com/YmidOrtega/Awaken-WoL"><b>📂 View repository »</b></a>
      </div>
    </td>
  </tr>
</table>

---

### Metrics & Activity

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/stats-en-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/stats-en.svg" />
    <img src="https://raw.githubusercontent.com/YmidOrtega/YmidOrtega/output/stats-en.svg" alt="YmidOrtega's activity over the last 12 months" />
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

### Let's talk
- 💼 **Availability:** Open to freelance projects, technical consulting or just to chat about technology.
- 🌐 **Website:** [ymid.me](https://www.ymid.me/)
- 📨 **Contact:** [yortegap7920@proton.me](mailto:yortegap7920@proton.me)
- 🔗 **LinkedIn:** [linkedin.com/in/ymidortega](https://www.linkedin.com/in/ymidortega/)
