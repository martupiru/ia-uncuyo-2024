---
title: tp7-cv

---

## Cross Validation
### Código create_folds
    create_folds <- function(df, k) {
      set.seed(42)  #semilla
      n <- nrow(df)
      folds <- sample(rep(1:k, length.out = n)) 
      
### Código cross_validation
        cross_validation <- function(df, k) {
      folds <- create_folds(df, k)

      #variables para almacenar metricas en cada fold
      accuracy_list <- c()
      precision_list <- c()
      sensitivity_list <- c()
      specificity_list <- c()

      for (i in 1:k) {
        #separar en datos de entrenamiento y prueba
        test_idx <- folds[[paste0("Fold", i)]]
        test_data <- df[test_idx, ]
        train_data <- df[-test_idx, ]

     #ajustar niveles para los factores en test_data
        test_data$ultima_modificacion <- factor(test_data$ultima_modificacion, levels = levels(train_data$ultima_modificacion))
        test_data$especie <- factor(test_data$especie, levels = levels(train_data$especie))  #ajustar niveles de 'especie'
    
    #entrenar el modelo de arboil de decision
    model <- rpart(inclinacion_peligrosa ~ ., data = train_data, method = "class")
    
    #realizar predicciones
    predictions <- predict(model, test_data, type = "class")
    test_data$prediction_class <- as.integer(predictions)  #agregar predicciones
    
    #calcular valores de la matriz de confusion
    tp <- sum(test_data$inclinacion_peligrosa == 1 & test_data$prediction_class == 1)
    tn <- sum(test_data$inclinacion_peligrosa == 0 & test_data$prediction_class == 0)
    fp <- sum(test_data$inclinacion_peligrosa == 0 & test_data$prediction_class == 1)
    fn <- sum(test_data$inclinacion_peligrosa == 1 & test_data$prediction_class == 0)
    
### Código para calcular métricas
        #calcular metricas y guardar
        accuracy_list <- c(accuracy_list, calculate_accuracy(tp, tn, fp, fn))
        precision_list <- c(precision_list, calculate_precision(tp, fp))
        sensitivity_list <- c(sensitivity_list, calculate_sensitivity(tp, fn))
        specificity_list <- c(specificity_list, calculate_specificity(tn, fp))
      }

      #calcular media y desv estandar para cada metrica
      results <- data.frame(
        "Metric" = c("Accuracy", "Precision", "Sensitivity", "Specificity"),
        "Mean" = c(mean(accuracy_list), mean(precision_list), mean(sensitivity_list), mean(specificity_list)),
        "Std_Dev" = c(sd(accuracy_list), sd(precision_list), sd(sensitivity_list), sd(specificity_list))
      )

      return(results)
    }
    
#### Tabla con métricas


| Métrica   | Media     | Desv. Estándatr |
| --------  | --------  | --------        |
|Accuracy	| 0.1100469	|   0.01207515    |	
|Precision	| 0.1100469	|   0.01207515	  |
|Sensitivity| 1.0000000 |	0.00000000	  |	
|Specificity| 0.0000000 |	0.00000000	  |