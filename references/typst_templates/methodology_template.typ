#set page(paper: "a4", margin: (x: 2.5cm, y: 2.5cm))
#set text(font: "Liberation Serif", size: 11pt)
#set par(justify: true, leading: 0.75em)

#align(center)[
  #text(16pt, weight: "bold")[#title] \
  #v(0.5em)
  #text(12pt)[*#author*] \
  #text(10pt)[#affiliation] \
  #text(9pt, fill: luma(100))[Date: #datetime.today().display()]
]

#v(1.5em)

= Research Methodology & Epistemological Framework

== 1. Research Design and Epistemology
#design_text

== 2. Target Population, Sampling Frame, and Sample Size
#sampling_text

== 3. Variable Operationalization and Measurement Scales
#variables_text

== 4. Data Collection Protocol and Instrument Validation
#instrument_text

== 5. Quantitative and Econometric Analytical Model
#analysis_text

== 6. Downside Controls, Robustness Checks, and Sensitivity Analysis
#robustness_text

#v(1.5em)
#line(length: 100%, stroke: 0.5pt + luma(150))
#align(center)[
  #text(9pt, fill: luma(120))[Generated with Academic Research Pipeline Co-Pilot]
]
