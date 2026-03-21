# Estado del Arte: Inteligencia Artificial en Mantenimiento Industrial en Colombia

## Fecha de elaboración: Julio 2025

---

## 1. Caso de Estudio Directo en Colombia: Grupo A (Multinacional Colombiana)

Un estudio reciente desarrollado por la Universidad de Luxemburgo en colaboración con **Grupo A**, una multinacional colombiana que opera en los sectores de **manufactura de equipos automotrices, maquinaria y minería**, aborda directamente el uso de IA para mantenimiento predictivo:

- Se utilizan **agentes basados en Large Language Models (LLMs)** para limpiar y estandarizar registros de mantenimiento (logs), mejorando la calidad de los datos para alimentar modelos de mantenimiento predictivo.
- El dataset fue recopilado entre **2021 y 2024** e incluye: número de placa de vehículo, ID de orden de trabajo, nombre del componente, código de acción, información del mecánico, timestamps, lecturas de odómetro, costos de mantenimiento y clasificación de sistema/subsistema.
- Se identificaron **6 tipos de ruido** en los datos industriales reales:
  1. Desalineación de identificadores de vehículos
  2. Vehículos fuera de flota
  3. Valores inválidos (typos)
  4. Valores faltantes
  5. Registros de prueba del sistema digital
  6. Fechas de finalización incorrectas
- Se evaluaron 6 LLMs de producción (Nemotron, GPT-OSS-20B, Kimi-K2, Qwen3, GPT-OSS-120B, GPT-5) en tareas de limpieza de datos.
- **Resultados**: Los LLMs son efectivos para tareas de limpieza genéricas (detección de valores faltantes: hasta 100%, valores inválidos: hasta 86%), pero tienen dificultades con errores específicos del dominio como inconsistencias temporales (0% de corrección en fechas incorrectas).
- **Barreras identificadas**: Restricciones económicas, escasez de datasets disponibles para reproducibilidad y falta de experiencia especializada en ciencia de datos.

### Referencia:
> Dimidov, V., Hawlader, F., Jafarnejad, S., & Frank, R. (2025). *Cleaning Maintenance Logs with LLM Agents for Improved Predictive Maintenance*. Annual Conference of the Prognostics and Health Management Society 2025. arXiv:2511.05311.
> **URL:** https://arxiv.org/html/2511.05311v1
> **Repositorio del framework:** https://github.com/sntubix/agentic-pdm-log-cleaning

---

## 2. Directrices y Políticas de IA en la Industria Colombiana

Un análisis de texto de **160 directrices industriales** sobre IA Generativa y LLMs en 14 sectores industriales a nivel global incluye dos empresas colombianas:

- **Procaps Group** (industria farmacéutica colombiana): Participa en paneles sobre digitalización e inteligencia artificial en manufactura farmacéutica, mostrando la participación de la industria farmacéutica colombiana en la adopción de IA.
- **1DOC3** (salud digital colombiana): Provee atención médica accesible a millones de hispanohablantes utilizando IA.

El estudio aborda cómo la IA impulsa el **mantenimiento predictivo, control de calidad, gestión de cadena de suministro y automatización de procesos** en diversos sectores industriales. Se destaca que las empresas de construcción como VINCI, Bouygues y Grupo ACS utilizan IA para mantenimiento predictivo, realidad virtual/aumentada y recopilación de datos de geolocalización.

### Referencia:
> Jiao, J., Afroogh, S., Chen, K., Atkinson, D., & Dhurandhar, A. (2025). *Generative AI and LLMs in Industry: A text-mining Analysis and Critical Evaluation of Guidelines and Policy Statements Across Fourteen Industrial Sectors*. arXiv:2501.00957.
> **URL:** https://arxiv.org/pdf/2501.00957

---

## 3. IA como Catalizador de Crecimiento para PyMEs (Aplicable al Contexto Colombiano)

Un paper extenso sobre la adopción de IA en Pequeñas y Medianas Empresas destaca aplicaciones directas en mantenimiento industrial:

### Mantenimiento Predictivo:
- Sensores recopilan datos operacionales de equipos (temperatura, vibración).
- Modelos de Machine Learning analizan estos datos para predecir cuándo un componente probablemente fallará.
- Esto permite programar mantenimiento proactivamente, previniendo fallas catastróficas y tiempos de inactividad costosos.

### Impacto Cuantificable:
- **91%** de las PyMEs con IA reportan aumento directo de ingresos.
- Hasta **30%** de reducción en costos operacionales.
- Más de **20 horas mensuales** ahorradas en tareas administrativas.
- Ahorro proyectado de **35,000 horas de trabajo anuales** con aumento de productividad del 25%.
- El mercado global de IA se proyecta de $233.46 mil millones (2024) a $1.77 billones (2032).

### Barreras para PyMEs:
- Incertidumbre sobre ROI y costos iniciales.
- Brecha de conocimientos y habilidades en IA.
- Calidad y disponibilidad de datos limitadas.

### Referencia:
> (2025). *Leveraging Artificial Intelligence as a Strategic Growth Catalyst for Small and Medium-sized Enterprises*. arXiv:2509.14532.
> **URL:** https://arxiv.org/html/2509.14532v1

---

## 4. Sistemas CoPilot Multi-Agente para Manufactura Inteligente (SmartPilot)

SmartPilot es un **CoPilot neurosimbólico multi-agente** diseñado para razonamiento avanzado y toma de decisiones contextual en manufactura, que aborda tres tareas críticas:

### Agentes Especializados:
1. **PredictX** (Predicción de Anomalías): Modelo de fusión multimodal que integra datos de series temporales (autoencoder) con datos de imagen (EfficientNet). Precisión del **93%** en predicción de anomalías.
2. **ForeSight** (Pronóstico de Producción): Modelo basado en LSTM que captura dependencias temporales e integra conocimiento específico del dominio. Mejora promedio del **21.51%** comparado con LSTM estándar.
3. **InfoGuide** (Q&A Específico del Dominio): Utiliza RAG (Retrieval-Augmented Generation) con modelos LLaMA-2-7b y Mixtral para responder preguntas técnicas de manufactura en tiempo real. Precisión del 88.6% y tiempo de respuesta promedio de 2.3 segundos.

### Características Técnicas:
- Integración de técnicas neurosimbólicas (Knowledge-Infused Learning).
- Modelos compactos optimizados para despliegue en dispositivos edge.
- Procesamiento de datos multimodales (series temporales, imágenes, texto).
- Conexión con servidor OPC-UA para datos de sensores en tiempo real.

### Referencia:
> (2025). *SmartPilot: A Multiagent CoPilot for Adaptive and Intelligent Manufacturing*. arXiv:2505.06492.
> **URL:** https://arxiv.org/html/2505.06492v1
> **Repositorio:** https://github.com/ChathurangiShyalika/SmartPilot

---

## 5. Gemelos Digitales con IA para Mantenimiento Industrial

Un survey comprehensivo sobre Digital Twin AI presenta un marco unificado de cuatro etapas para la integración de IA en gemelos digitales:

### Aplicaciones en Mantenimiento:
- **Rolls-Royce**: Utiliza gemelos digitales para personalizar procesos de reparación de partes de motores, automatizando y optimizando prácticas de mantenimiento.
- **Boeing**: Emplea gemelos digitales para sistemas de baterías del 787 Dreamliner para mejorar seguridad y gestión de riesgos.
- **Airbus**: Usa gemelos digitales para el A350 XWB para monitoreo de rendimiento en tiempo real, mejorando eficiencia de combustible y reduciendo emisiones.

### Marco de Cuatro Etapas:
1. **Modelado** del gemelo físico (métodos basados en física y IA informada por física).
2. **Espejamiento** del sistema físico al gemelo digital con sincronización en tiempo real.
3. **Intervención** mediante modelado predictivo, detección de anomalías y optimización.
4. **Gestión autónoma** mediante LLMs, modelos fundacionales y agentes inteligentes.

### Técnicas de IA para Mantenimiento Predictivo:
- Redes neuronales convolucionales (CNNs), recurrentes (RNNs) y de grafos (GNNs).
- Autoencoders, GANs y modelos híbridos para detección de anomalías.
- Aprendizaje por refuerzo para control adaptativo y optimización en tiempo real.

### Referencia:
> (2025). *Digital Twin AI: Opportunities and Challenges from Large Language Models to World Models*. arXiv:2601.01321.
> **URL:** https://arxiv.org/html/2601.01321v1

---

## 6. Despliegue y Monitoreo de Modelos ML en la Industria (Encuesta Internacional con Participación Colombiana)

Una encuesta internacional con **188 respuestas completas de 25 países** (incluyendo **Colombia con 3 respuestas**, y Brasil con 72) sobre prácticas de ingeniería de sistemas con ML:

### Hallazgos Clave sobre Despliegue:
- **59.5%** despliegan modelos como servicios separados.
- **42.7%** utilizan modelos embebidos dentro de la aplicación.
- Solo **29%** siguen prácticas y principios de MLOps.
- Menos del **50%** de los proyectos de ML llegan a producción.

### Problemas Principales en Despliegue:
- Preparación de infraestructura para despliegue en producción.
- Integración con aplicaciones legadas.
- Definición de arquitectura de infraestructura.
- Escalabilidad y limitaciones financieras.

### Hallazgos sobre Monitoreo:
- **33%** reporta que menos del 20% de los modelos en producción están monitoreados.
- Aspectos más monitoreados: Entradas/Salidas (62.7%) y Decisiones (62.1%).
- Problemas: Ausencia de prácticas de monitoreo, necesidad de herramientas personalizadas, selección de métricas apropiadas.

### Referencia:
> Zimelewicz, E., Kalinowski, M., Mendez, D., Giray, G., Alves, A.P.S., et al. (2024). *ML-Enabled Systems Model Deployment and Monitoring: Status Quo and Problems*. SWQD 2024. arXiv:2402.05333.
> **URL:** https://arxiv.org/pdf/2402.05333
> **Datos abiertos:** https://doi.org/10.5281/zenodo.10092394

---

## 7. Política Nacional de IA en Colombia (Contexto Regulatorio)

Colombia ha avanzado significativamente en su marco político para la IA:

### Política Nacional de IA (CONPES 4144 - Febrero 2025):
- **6 ejes estratégicos** y **106 acciones**.
- Busca definir condiciones habilitantes para el aprovechamiento de la IA.
- Aborda problemas sociales, económicos y ambientales.
- Propone regulaciones para mitigar riesgos de la IA.
- Planea ejecutarse hasta **2030**.

### Plan de Acción de Biodiversidad (PAB - Octubre 2024):
- 4 apuestas, 6 metas nacionales y 191 acciones.
- La convergencia temporal de ambas políticas crea oportunidades de inversión financiera conjunta entre sectores de IA y otros sectores productivos.

### Referencia:
> Cañas, J.S., Parra-Guevara, C., Montoya-Castrillón, M., et al. (2025). *Inteligencia Artificial para la conservación y uso sostenible de la biodiversidad, una visión desde Colombia*. arXiv:2503.14543.
> **URL:** https://arxiv.org/html/2503.14543v1
> **Referencia de política:** DNP (2025). Política Nacional de Inteligencia Artificial (CONPES 4144). Departamento Nacional de Planeación de Colombia.

---

## 8. IA para Mantenimiento Predictivo en Canteras (Contexto Hispanohablante)

Un paper presentado en **Tecniacústica 2023** (Cuenca, España) aborda el uso de **procesamiento de señales acústicas con IA** para mantenimiento predictivo en canteras, directamente relevante para el sector minero colombiano.

- Utiliza modelado de señales acústicas para detectar anomalías en equipos de canteras.
- Aplicación de técnicas de procesamiento de audio con deep learning.
- Relevante para sectores de minería y extracción en Colombia.

### Referencia:
> (2023). *IA Para el Mantenimiento Predictivo en Canteras: Modelado*. Presentado en Tecniacústica 2023. arXiv:2310.16140.
> **URL:** https://arxiv.org/abs/2310.16140

---

## 9. Contexto de IA en Colombia: Visión desde el Instituto Humboldt

Aunque no es específicamente sobre mantenimiento industrial, este paper provee un diagnóstico crucial del **ecosistema de IA en Colombia**:

### Hallazgos Relevantes:
- Colombia ha experimentado un crecimiento exponencial de la IA en la industria, impulsando innovación en **salud, manufactura, finanzas, transporte y comunicación**.
- Los principales desafíos para la implementación de IA en Colombia incluyen:
  - Subrepresentación de datos en la región.
  - Limitaciones financieras y logísticas.
  - Necesidad de modelos adaptados al contexto local.
  - Brecha entre ciencias de la computación y dominio de aplicación.
- Se enfatiza la importancia de **colaboraciones interdisciplinarias** y el desarrollo de herramientas de código abierto.
- Iniciativas como **Khipu** (Latin American Meeting in AI) y **LatinX in AI** promueven la capacitación en IA en América Latina.

### Referencia:
> Cañas, J.S., et al. (2025). *Inteligencia Artificial para la conservación y uso sostenible de la biodiversidad, una visión desde Colombia*. Instituto de Investigación de Recursos Biológicos Alexander von Humboldt. arXiv:2503.14543.
> **URL:** https://arxiv.org/html/2503.14543v2

---

## Resumen de Temas Clave para el Estado del Arte

| # | Tema | Descripción | Fuentes Clave |
|---|------|-------------|---------------|
| 1 | Mantenimiento Predictivo con ML | Uso de sensores IoT + modelos de ML para predecir fallas en equipos industriales | Dimidov et al. (2025), SmartPilot (2025) |
| 2 | LLMs para limpieza de datos industriales | Agentes basados en LLMs para curar y estandarizar logs de mantenimiento | Dimidov et al. (2025) |
| 3 | Gemelos Digitales | Réplicas virtuales de equipos para simulación, predicción y optimización | Digital Twin AI (2025) |
| 4 | Sistemas Multi-Agente | CoPilots con agentes especializados en anomalías, pronóstico y Q&A | SmartPilot (2025) |
| 5 | Barreras en Colombia | Calidad de datos, integración de sistemas legados, talento en IA, costos | Dimidov et al. (2025), Zimelewicz et al. (2024) |
| 6 | Política Pública | CONPES 4144 (2025) como marco regulatorio habilitante para IA en Colombia | DNP (2025), Cañas et al. (2025) |
| 7 | MLOps | Baja adopción de pipelines automatizados de reentrenamiento y monitoreo | Zimelewicz et al. (2024) |
| 8 | IA en PyMEs | Impacto cuantificable de IA en productividad y reducción de costos | arXiv:2509.14532 (2025) |
| 9 | Procesamiento acústico | IA para análisis de señales acústicas en mantenimiento predictivo | arXiv:2310.16140 (2023) |

---

## Lista Completa de Referencias Bibliográficas

1. Dimidov, V., Hawlader, F., Jafarnejad, S., & Frank, R. (2025). *Cleaning Maintenance Logs with LLM Agents for Improved Predictive Maintenance*. arXiv:2511.05311. https://arxiv.org/html/2511.05311v1

2. Jiao, J., Afroogh, S., Chen, K., Atkinson, D., & Dhurandhar, A. (2025). *Generative AI and LLMs in Industry: A text-mining Analysis and Critical Evaluation of Guidelines and Policy Statements Across Fourteen Industrial Sectors*. arXiv:2501.00957. https://arxiv.org/pdf/2501.00957

3. (2025). *Leveraging Artificial Intelligence as a Strategic Growth Catalyst for Small and Medium-sized Enterprises*. arXiv:2509.14532. https://arxiv.org/html/2509.14532v1

4. (2025). *SmartPilot: A Multiagent CoPilot for Adaptive and Intelligent Manufacturing*. arXiv:2505.06492. https://arxiv.org/html/2505.06492v1

5. (2025). *Digital Twin AI: Opportunities and Challenges from Large Language Models to World Models*. arXiv:2601.01321. https://arxiv.org/html/2601.01321v1

6. Zimelewicz, E., Kalinowski, M., Mendez, D., et al. (2024). *ML-Enabled Systems Model Deployment and Monitoring: Status Quo and Problems*. SWQD 2024. arXiv:2402.05333. https://arxiv.org/pdf/2402.05333

7. Cañas, J.S., Parra-Guevara, C., Montoya-Castrillón, M., et al. (2025). *Inteligencia Artificial para la conservación y uso sostenible de la biodiversidad, una visión desde Colombia*. arXiv:2503.14543. https://arxiv.org/html/2503.14543v1

8. (2023). *IA Para el Mantenimiento Predictivo en Canteras: Modelado*. Tecniacústica 2023. arXiv:2310.16140. https://arxiv.org/abs/2310.16140

9. DNP (2025). *Política Nacional de Inteligencia Artificial (CONPES 4144)*. Departamento Nacional de Planeación de Colombia.

---

*Documento generado como apoyo para trabajo de grado de maestría.*
*Las fuentes fueron obtenidas mediante búsqueda en bases de datos académicas (arXiv, Tavily) en julio de 2025.*
