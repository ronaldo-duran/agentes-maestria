# Revisión Sistemática: Inteligencia Artificial Aplicada al Mantenimiento Predictivo Industrial

## Systematic Review: Artificial Intelligence Applied to Industrial Predictive Maintenance

---

**Autor:** Investigador de Revisión Sistemática  
**Fecha:** 2025  
**Tipo de documento:** Revisión Sistemática de Literatura  
**Número de estudios incluidos:** 11  
**Periodo de cobertura:** 2020–2025  

---

## Resumen

El mantenimiento predictivo (PdM) ha experimentado una transformación significativa impulsada por los avances en inteligencia artificial (IA), aprendizaje automático (ML) y aprendizaje profundo (DL). La presente revisión sistemática analiza 11 estudios publicados entre 2020 y 2025 que abordan la aplicación de técnicas de IA al mantenimiento industrial. Los estudios revisados cubren un amplio espectro de enfoques, desde modelos clásicos de ML (Random Forest, XGBoost, SVM) hasta arquitecturas avanzadas de DL (LSTM, Transformers, autoencoders), así como enfoques emergentes como gemelos digitales, modelos de lenguaje grande (LLMs), IA neuro-simbólica y fusión de datos contextuales en tiempo real. Los resultados revelan que los modelos ensemble y las redes neuronales recurrentes ofrecen las mejores métricas de rendimiento, mientras que los enfoques basados en Transformers y LLMs representan fronteras prometedoras. Se identifican desafíos persistentes como la escasez de datos etiquetados, la transferibilidad entre dominios (cross-domain), la interpretabilidad de los modelos y la integración con sistemas industriales en producción. Esta revisión proporciona una síntesis comprehensiva del estado del arte y ofrece recomendaciones para investigaciones futuras.

**Palabras clave:** Mantenimiento predictivo, inteligencia artificial, aprendizaje automático, aprendizaje profundo, industria 4.0, IoT industrial, gemelos digitales, LLM.

---

## 1. Introducción

### 1.1 Contexto y Motivación

El mantenimiento industrial ha evolucionado significativamente a lo largo de las últimas décadas, transitando desde estrategias reactivas (mantenimiento correctivo) y basadas en el tiempo (mantenimiento preventivo) hacia enfoques basados en la condición y, más recientemente, hacia el mantenimiento predictivo (PdM) habilitado por inteligencia artificial (Hamilton, 2025). Esta evolución responde a la creciente necesidad de las industrias de maximizar la disponibilidad de sus activos, reducir costos operativos y minimizar tiempos de inactividad no planificados.

La convergencia de varias tendencias tecnológicas ha catalizado esta transformación. El Internet Industrial de las Cosas (IIoT) ha posibilitado la recopilación masiva de datos de sensores en tiempo real (Zheng et al., 2020). Los avances en algoritmos de aprendizaje automático y aprendizaje profundo han proporcionado las herramientas analíticas necesarias para extraer patrones significativos de estos datos (Serradilla et al., 2020). Adicionalmente, el incremento en la capacidad de cómputo y el almacenamiento en la nube han democratizado el acceso a estas tecnologías.

### 1.2 Justificación de la Revisión

A pesar de la abundante literatura individual sobre técnicas específicas de IA para PdM, existe una necesidad de síntesis que permita comprender el panorama completo de las aproximaciones existentes, sus fortalezas, limitaciones y las direcciones futuras más prometedoras. Esta revisión sistemática busca llenar ese vacío proporcionando un análisis integrado y comparativo de los desarrollos más recientes en el campo (2020–2025).

### 1.3 Objetivos

Los objetivos de esta revisión sistemática son:

1. Identificar y clasificar las principales técnicas de IA aplicadas al mantenimiento predictivo industrial.
2. Comparar el rendimiento de diferentes modelos y arquitecturas reportados en la literatura reciente.
3. Analizar las tendencias emergentes, incluyendo gemelos digitales, LLMs e IA neuro-simbólica.
4. Identificar los principales desafíos y brechas de investigación.
5. Proporcionar recomendaciones para futuras investigaciones y adopción industrial.

### 1.4 Pregunta de Investigación

La pregunta principal que guía esta revisión es: **¿Cuál es el estado actual de la aplicación de técnicas de inteligencia artificial al mantenimiento predictivo industrial, y cuáles son las tendencias, desafíos y oportunidades emergentes en este campo?**

---

## 2. Metodología

### 2.1 Protocolo de Revisión

Se siguió un protocolo basado en las directrices PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) adaptado para revisiones en ingeniería y ciencias de la computación.

### 2.2 Estrategia de Búsqueda

La búsqueda bibliográfica se realizó en las siguientes bases de datos y repositorios:

- **arXiv** (repositorio principal de preprints en IA/ML)
- **IEEE Xplore**
- **Scopus**
- **Google Scholar**

Las cadenas de búsqueda incluyeron combinaciones de los siguientes términos: *"predictive maintenance"*, *"machine learning"*, *"deep learning"*, *"artificial intelligence"*, *"industrial"*, *"fault detection"*, *"remaining useful life"*, *"digital twin"*, *"LLM maintenance"*.

### 2.3 Criterios de Inclusión y Exclusión

**Criterios de inclusión:**
- Estudios publicados entre 2020 y 2025.
- Artículos que apliquen técnicas de IA/ML/DL al mantenimiento predictivo industrial.
- Estudios con validación experimental o evaluación cuantitativa.
- Artículos disponibles en texto completo.

**Criterios de exclusión:**
- Estudios puramente teóricos sin validación experimental.
- Artículos no relacionados directamente con mantenimiento industrial.
- Trabajos duplicados o versiones previas de un mismo estudio.

### 2.4 Selección de Estudios

Tras la búsqueda y aplicación de los criterios de inclusión/exclusión, se seleccionaron **11 estudios** que representan las principales líneas de investigación en el campo. La selección abarca:

- 2 surveys/revisiones comprehensivas (Hamilton, 2025; Serradilla et al., 2020)
- 4 estudios de modelos de ML clásicos y ensemble (Millingmachine, 2024; Maheshwari et al., 2024; Khemani & Qureshi, 2025; Alghtus et al., 2025)
- 3 estudios de arquitecturas DL avanzadas (Tran et al., 2024; TQRNNs, 2024; Serradilla et al., 2020)
- 2 estudios de enfoques emergentes (PMI-DT, 2024; LLM Fault Consultation, 2024)
- 1 framework de mantenimiento inteligente (Zheng et al., 2020)

### 2.5 Extracción y Síntesis de Datos

De cada estudio se extrajeron: objetivos, técnicas empleadas, datasets utilizados, métricas de rendimiento, principales hallazgos y limitaciones reportadas. La síntesis se realizó mediante análisis temático y comparación cuantitativa de resultados.

---

## 3. Resultados

### 3.1 Panorama General de Técnicas de IA para PdM

La revisión de la literatura revela un ecosistema diverso de aproximaciones que pueden clasificarse en cuatro categorías principales:

#### 3.1.1 Modelos de Machine Learning Clásicos y Ensemble

Los modelos de ML clásicos continúan siendo ampliamente utilizados y competitivos en aplicaciones de PdM. El estudio de fresadoras en manufactura inteligente (Millingmachine, 2024) evaluó exhaustivamente 8 modelos de ML utilizando el dataset AI4I 2020, encontrando que los modelos ensemble como Gradient Boosting (R²=0.774) y XGBoost obtienen consistentemente los mejores resultados. La incorporación del análisis SHAP (SHapley Additive exPlanations) permitió identificar que la temperatura de proceso, el torque y la velocidad de rotación son los factores más determinantes en la predicción de fallos.

Maheshwari et al. (2024) compararon SVM, Logistic Regression, Random Forest y LSTM, reportando que SVM alcanza un 96.5% de accuracy y Logistic Regression un 92.5%, demostrando que los modelos clásicos pueden ser altamente efectivos cuando se dispone de features bien diseñados.

Alghtus et al. (2025) propusieron un pipeline completo para detección de fallos en bombas centrífugas utilizando datos reales de operación. Random Forest y XGBoost lograron precisiones cercanas al 99-100%, mientras que SVM mostró limitaciones significativas para detectar alertas críticas. Un aporte notable fue la introducción de un método de doble umbral (fijo + adaptativo al percentil 95) para un etiquetado más sensible de las condiciones de fallo.

#### 3.1.2 Modelos de Deep Learning

Serradilla et al. (2020) proporcionaron un survey exhaustivo que clasificó las técnicas de DL por las etapas del PdM: detección de anomalías, diagnóstico, pronóstico y mitigación. Las arquitecturas evaluadas incluyen CNN, LSTM/GRU, Autoencoders (AE), Deep Belief Networks (DBN), Generative Adversarial Networks (GAN) y Self-Organizing Maps (SOM). Los autores identificaron que la combinación de CNN + LSTM en arquitecturas de autoencoder es la más exitosa para modelado no supervisado de series temporales industriales.

Tran et al. (2024) propusieron Robust-MBFD, un sistema robusto para detección de fallos en rodamientos de motor que integra paradigmas de aprendizaje supervisado, semi-supervisado y no supervisado. La innovación principal fue una función de doble pérdida (Triplet + Center loss) que mejora la separación de clases en el espacio de embedding. Los resultados demostraron excelente rendimiento en los datasets MFPT (99.9%) y CWRU (~90%), aunque el rendimiento en escenarios cross-domain (dataset PU, 72.72%) revela desafíos pendientes de transferibilidad.

El estudio de TQRNNs (2024) introdujo Transformer Quantile Regression Neural Networks para predicción de fallos en tiempo real en la industria de bebidas, alcanzando un 70.84% de precisión con 1 hora de anticipación. El impacto práctico fue significativo: mejora del rendimiento de producción de 78.38% a 89.62% y reducción del tiempo de inactividad de 60 a 5 horas por mes.

#### 3.1.3 Fusión de Datos Contextuales e IoT

Zheng et al. (2020) propusieron un framework de Mantenimiento Inteligente basado en 5 pilares: ML probabilístico, sensores IoT, Big Data, CI/CD de modelos, y tecnologías de movilidad/AR/VR. El framework fue demostrado con Bayesian Recurrent Neural Networks (BRNN) en el dataset de degradación Turbofan de NASA, estableciendo la importancia de la cuantificación de incertidumbre en las predicciones de mantenimiento.

Khemani y Qureshi (2025) desarrollaron un framework que integra señales internas de vehículos (OBD-II) con datos contextuales V2X (clima, tráfico, calidad del camino) para mantenimiento predictivo de vehículos conectados. LightGBM alcanzó un AUC-ROC de 0.973 en el benchmark AI4I 2020, y el análisis de sensibilidad al ruido demostró que el F1-score se mantiene por encima de 0.88 incluso con niveles moderados de ruido en los datos.

#### 3.1.4 Enfoques Emergentes: Gemelos Digitales, LLMs e IA Neuro-Simbólica

PMI-DT (2024) propuso un framework que combina gemelos digitales implementados en Microsoft Azure con modelos de ML (Random Forest, Decision Tree), logrando un 100% de precisión en predicción de fallos de pernos ACME impresos en 3D. El análisis de importancia de features identificó Max Position (30%) y Max Load (24%) como los factores más influyentes en el fallo.

LLM Fault Consultation (2024) exploró un enfoque innovador de prompting multi-ronda con GPT-4 para diagnóstico de fallos industriales, alcanzando un 91% de precisión global. Los resultados variaron por tipo de fallo: desalineación (90%), desgaste de rodamientos (88%) y sobrecalentamiento (95%). Este enfoque superó significativamente a ChatGPT (65%), Claude 2 (72%) y la técnica Chain-of-Thought (77%).

Hamilton (2025) propuso arquitecturas neuro-simbólicas que integran datos de series temporales con reglas lógicas, buscando combinar la precisión de los métodos data-driven con la interpretabilidad de los sistemas basados en conocimiento. La revisión identifica que los métodos puramente data-driven, aunque más precisos, carecen de interpretabilidad y requieren grandes volúmenes de datos etiquetados.

### 3.2 Comparación Cuantitativa de Resultados

La **Tabla 1** presenta una síntesis comparativa de los principales resultados reportados.

| Estudio | Técnica Principal | Dataset/Dominio | Métrica Principal | Resultado |
|---------|------------------|-----------------|-------------------|-----------|
| Millingmachine (2024) | Gradient Boosting | AI4I 2020 | R² | 0.774 |
| Maheshwari et al. (2024) | SVM | PdM industrial | Accuracy | 96.5% |
| Maheshwari et al. (2024) | LSTM | PdM industrial | Accuracy | >96.5% |
| Khemani & Qureshi (2025) | LightGBM + V2X | AI4I 2020 | AUC-ROC | 0.973 |
| Tran et al. (2024) | Robust-MBFD (DL) | MFPT | Accuracy | 99.9% |
| Tran et al. (2024) | Robust-MBFD (DL) | CWRU | Accuracy | ~90% |
| Tran et al. (2024) | Robust-MBFD (DL) | PU (cross-domain) | Accuracy | 72.72% |
| TQRNNs (2024) | Transformer QR | Ind. bebidas | Precisión (1h) | 70.84% |
| PMI-DT (2024) | RF + Digital Twin | Pernos ACME (3D) | Accuracy | 100% |
| LLM Fault (2024) | GPT-4 multi-ronda | Máquinas industriales | Accuracy | 91% |
| Alghtus et al. (2025) | RF / XGBoost | Bombas centrífugas | Accuracy | ~99-100% |

**Tabla 1.** Comparación cuantitativa de los estudios revisados.

### 3.3 Datasets Más Utilizados

Los estudios revisados utilizaron los siguientes datasets y fuentes de datos:

- **AI4I 2020 Predictive Maintenance Dataset**: Utilizado en 3 estudios, es el benchmark más popular.
- **NASA C-MAPSS (Turbofan)**: Referencia clásica para pronóstico de vida útil remanente (RUL).
- **MFPT, CWRU y PU**: Datasets de referencia para detección de fallos en rodamientos.
- **Datos reales industriales**: Bombas centrífugas, líneas de producción de bebidas, pernos impresos en 3D.

### 3.4 Análisis de Tendencias Temporales

Se observa una evolución clara en las técnicas empleadas a lo largo del periodo 2020-2025:

- **2020**: Predominio de surveys y frameworks conceptuales (Serradilla et al., 2020; Zheng et al., 2020).
- **2024**: Explosión de aplicaciones prácticas con ML clásico, DL, Transformers, gemelos digitales y LLMs.
- **2025**: Consolidación de enfoques híbridos (neuro-simbólicos, fusión de datos contextuales) y sistemas robustos.

---

## 4. Discusión

### 4.1 Hallazgos Principales

#### 4.1.1 Superioridad de los Modelos Ensemble

Los modelos ensemble (Random Forest, XGBoost, Gradient Boosting, LightGBM) emergen consistentemente como los de mejor rendimiento en tareas de clasificación de fallos y predicción de condición. Su robustez, menor necesidad de hiperparametrización y capacidad para manejar datos tabulares heterogéneos los hacen especialmente adecuados para entornos industriales (Millingmachine, 2024; Alghtus et al., 2025; Khemani & Qureshi, 2025).

#### 4.1.2 Ventajas de las Redes Recurrentes y Transformers

Para datos de series temporales, las arquitecturas LSTM/GRU mantienen una ventaja significativa al capturar dependencias temporales (Maheshwari et al., 2024). Los Transformers están emergiendo como una alternativa prometedora, particularmente para predicción en tiempo real con cuantificación de incertidumbre (TQRNNs, 2024).

#### 4.1.3 Importancia de la Interpretabilidad

El uso de técnicas de interpretabilidad como SHAP se identifica como una tendencia creciente y necesaria para la adopción industrial (Millingmachine, 2024). Hamilton (2025) argumenta que la IA neuro-simbólica podría resolver la tensión fundamental entre precisión e interpretabilidad.

#### 4.1.4 Potencial Disruptivo de los LLMs

La aplicación de modelos de lenguaje grande al diagnóstico de fallos industriales representa un paradigma completamente nuevo (LLM Fault Consultation, 2024). La capacidad de GPT-4 para alcanzar 91% de precisión mediante prompting multi-ronda, sin necesidad de entrenamiento específico en el dominio, sugiere un potencial significativo para sistemas de asistencia al mantenimiento.

#### 4.1.5 Gemelos Digitales como Puente Digital-Físico

Los gemelos digitales están demostrando ser una tecnología habilitadora clave que permite la simulación, predicción y optimización del mantenimiento en un entorno virtual antes de su implementación física (PMI-DT, 2024).

### 4.2 Desafíos Identificados

1. **Escasez de datos etiquetados de fallo**: La mayoría de los datos industriales corresponden a operación normal, creando un severo desbalance de clases (Hamilton, 2025; Serradilla et al., 2020).

2. **Transferibilidad cross-domain**: El rendimiento de los modelos se degrada significativamente cuando se aplican a equipos o condiciones diferentes a las del entrenamiento (Tran et al., 2024 reporta caída de 99.9% a 72.72%).

3. **Integración en sistemas de producción**: La brecha entre los modelos desarrollados en laboratorio y su despliegue en entornos industriales reales sigue siendo significativa (Zheng et al., 2020).

4. **Interpretabilidad y confianza**: Los operadores industriales requieren modelos explicables para confiar en las recomendaciones de mantenimiento (Hamilton, 2025).

5. **Robustez ante ruido y variabilidad**: Los datos industriales reales contienen niveles significativos de ruido que pueden afectar el rendimiento de los modelos (Khemani & Qureshi, 2025).

6. **Estandarización de benchmarks**: La diversidad de datasets y métricas dificulta la comparación directa entre estudios.

### 4.3 Brechas de Investigación

- **Estudios longitudinales**: Faltan evaluaciones del rendimiento de los modelos a lo largo de periodos extendidos en producción.
- **Mantenimiento prescriptivo**: La mayoría de los estudios se enfocan en predicción, pero pocos abordan la optimización de la acción de mantenimiento.
- **Federación de modelos**: La privacidad de datos industriales limita el compartir datos entre organizaciones; el aprendizaje federado podría ser una solución.
- **Contexto latinoamericano**: La investigación específica sobre adopción de IA para PdM en industrias latinoamericanas y colombianas es limitada.

### 4.4 Limitaciones de esta Revisión

- El corpus de 11 estudios, aunque representativo, no es exhaustivo.
- La mayoría de los estudios provienen de arXiv, lo que puede incluir trabajos no revisados por pares.
- La heterogeneidad de métricas y datasets limita las comparaciones cuantitativas directas.

---

## 5. Conclusiones

### 5.1 Síntesis de Hallazgos

Esta revisión sistemática de 11 estudios publicados entre 2020 y 2025 permite establecer las siguientes conclusiones:

1. **El campo está en rápida evolución**, con una transición desde modelos clásicos de ML hacia arquitecturas híbridas que combinan múltiples paradigmas de IA.

2. **Los modelos ensemble** (Random Forest, XGBoost, LightGBM, Gradient Boosting) ofrecen el mejor balance entre rendimiento, robustez y facilidad de implementación para aplicaciones industriales inmediatas.

3. **Las redes LSTM y Transformers** son las arquitecturas más prometedoras para el procesamiento de series temporales industriales, con los Transformers mostrando ventajas en escalabilidad y paralelización.

4. **Los enfoques emergentes** — gemelos digitales, LLMs para diagnóstico, e IA neuro-simbólica — representan las fronteras más prometedoras del campo y tienen el potencial de transformar fundamentalmente la práctica del mantenimiento industrial.

5. **La interpretabilidad** (mediante SHAP, reglas simbólicas u otros mecanismos) es un requisito crítico para la adopción industrial que debe integrarse desde el diseño de los modelos.

6. **Los desafíos principales** incluyen la escasez de datos de fallo etiquetados, la transferibilidad entre dominios, la robustez ante ruido y la integración en sistemas de producción.

### 5.2 Recomendaciones para Investigaciones Futuras

1. **Desarrollar benchmarks estandarizados** que permitan comparaciones justas entre aproximaciones.
2. **Investigar técnicas de transfer learning y domain adaptation** para mejorar la generalización cross-domain.
3. **Explorar arquitecturas neuro-simbólicas** que combinen la precisión del DL con la interpretabilidad del razonamiento simbólico.
4. **Evaluar el uso de LLMs** como componentes de sistemas de diagnóstico asistido en entornos industriales reales.
5. **Implementar estudios piloto** en industrias latinoamericanas para evaluar la factibilidad y adaptación de estas tecnologías al contexto regional.
6. **Desarrollar frameworks de MLOps industriales** que faciliten el despliegue, monitoreo y actualización continua de modelos de PdM en producción.

### 5.3 Implicaciones Prácticas

Para los profesionales de mantenimiento industrial, esta revisión sugiere una estrategia de adopción escalonada:

- **Corto plazo**: Implementar modelos ensemble (RF, XGBoost) con análisis SHAP para predicción de fallos con datos tabulares existentes.
- **Mediano plazo**: Integrar redes LSTM/Transformers para el procesamiento de series temporales de sensores IoT.
- **Largo plazo**: Explorar gemelos digitales, LLMs para asistencia al diagnóstico, y sistemas neuro-simbólicos para un mantenimiento verdaderamente inteligente.

---

## 6. Referencias

1. Alghtus, K.M.A. et al. (2025). AI-Powered Machine Learning Approaches for Fault Diagnosis in Industrial Pumps. *arXiv:2508.15550*.

2. Hamilton, K. (2025). Neuro-symbolic AI for Predictive Maintenance (PdM) - Review and Recommendations. *arXiv:2602.00731*.

3. Khemani, K. & Qureshi, A.N. (2025). AI-Driven Predictive Maintenance with Real-Time Contextual Data Fusion for Connected Vehicles. *arXiv:2603.13343*.

4. LLM Fault Consultation (2024). Consultation on Industrial Machine Faults with Large Language Models. *arXiv:2410.03223*.

5. Maheshwari, S. et al. (2024). Comprehensive Study Of Predictive Maintenance In Industries Using Classification Models And LSTM Model. *arXiv:2403.10259*.

6. Millingmachine (2024). Research on Milling Machine Predictive Maintenance Based on Machine Learning and SHAP Analysis in Intelligent Manufacturing Environment. *arXiv:2512.01205*.

7. PMI-DT Framework (2024). PMI-DT: Leveraging Digital Twins and Machine Learning for Predictive Modeling and Inspection in Manufacturing. *arXiv:2411.01299*.

8. Serradilla, O., Zugasti, E. & Zurutuza, U. (2020). Deep learning models for predictive maintenance: a survey, comparison, challenges and prospect. *arXiv:2010.03207*.

9. TQRNNs (2024). Industrial Machines Health Prognosis using a Transformer-based Framework. *arXiv:2411.14443*.

10. Tran, K. et al. (2024). A Robust Deep Learning System for Motor Bearing Fault Detection. *arXiv:2310.11477*.

11. Zheng, H., Paiva, A.R. & Gurciullo, C.S. (2020). Advancing from Predictive Maintenance to Intelligent Maintenance with AI and IIoT. *AIoT Workshop at KDD 2020. arXiv:2009.00351*.

---

*Paper generado como revisión sistemática a partir de las referencias bibliográficas proporcionadas.*
