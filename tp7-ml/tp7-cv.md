# TP7
### Lucas Moyano

## A
### create folds
```
create_folds <- function(df, nFolds){
  #df tiene que ser mezclada anteriormente, este algoritmo no lo mezcla
  tamanio_folds = trunc(nrow(df)/nFolds)
  i=1
  lista <- list()
  while(i <= nFolds){
    if(i != nFolds){ #recolectamos los ids del dataframe mezclado
      tibble1 <- df[(((i*tamanio_folds)+1)-tamanio_folds):(tamanio_folds*i), 1]
      lista <- c(lista,list(tibble1[[1]]))
    } else {
      tibble1 <- df[(((i*tamanio_folds)+1)-tamanio_folds):nrow(df), 1]
      lista <- c(lista,list(tibble1[[1]]))
      }
    #if(i != nFolds){
      #lista <- c(lista,list((((i*tamanio_folds)+1)-tamanio_folds):(tamanio_folds*i)))
    #} else {
      #lista <- c(lista,list((((i*tamanio_folds)+1)-tamanio_folds):nrow(df)))
      #}
    i=i+1
  }
  return(lista)
}
```
### cross validation
```
cross_validation <- function(df, nFolds){
  #shuffle
  df <- df[sample(1:nrow(df)), ] #mezclamos las filas
  View(df)
  #creamos los folds
  folds = create_folds(df, nFolds)
  
  resultado = c("Accuracy", "Precision", "Sensitivity", "Specificity")
  k= 1
  while(k <= nFolds){
    fold <- folds[[k]]
    
    #removemos k elementos de la lista y los agregamos a los de test
    i=1
    foldR = list()
    while(i <= k){
      len_fold=length(fold)
      foldR <-append(foldR, fold[len_fold])
      fold <- fold[-len_fold]
      i=i+1
    }

    training1 <- subset(df, id %in% fold)
    test1 <- subset(df, id %in% foldR)
    
    # seleccionamos la clase y las variables que nos interesan
    train_formula<-formula(inclinacion_peligrosa~
                             circ_tronco_cm+
                             lat+long+
                             seccion)
    
    # generamos el modelo
    tree_model<-rpart(train_formula, data=training1, method='class')
    # obtenemos la predicción
    p<-predict(tree_model,test1,type='class')
    test1$prediction_class = p
    View(test1)
    confusion_matrix1 <- confusion_matrix(test1)
    columna <- c(Accuracy(confusion_matrix1), Precision(confusion_matrix1), Sensitivity(confusion_matrix1), Specificity(confusion_matrix1))
    nombre <- paste(as.character(k), " iterarion")
    resultado[nombre] <- columna
    k = k+1
  }
  
  i=2
  columna1 = c()
  columna2 = c()
  while(i <= length(resultado)){
    promedio = mean(resultado[i,-1])
    deviacion = sd(resultado[i,-1])
    i= i + 1
    columna1 = c(columna1, promedio)
    columna2 = c(columna2, deviacion)
  }
  return(data.frame(columna1,columna2))
  
}
```

## B
