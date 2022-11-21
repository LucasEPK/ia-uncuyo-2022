library(ggplot2)
library(cowplot)
library(randomForest)
library(readr)
library(dplyr)
library(tidyr)
library(caret)
#leemos los 2 datasets que tenemos
data_train <- read_csv("Universidad/2022 2ndo semestre/Inteligencia artificial/tp7-ml/arbolado mdz/arbolado-mza-dataset.csv/arbolado-mza-dataset.csv",
                       col_types = cols(
                         id = col_integer(),
                         especie = col_character(),
                         ultima_modificacion = col_character(),
                         altura = col_factor(),
                         circ_tronco_cm = col_double(),
                         diametro_tronco = col_factor(),
                         long = col_double(),
                         lat = col_double(),
                         seccion = col_integer(),
                         nombre_seccion = col_character(),
                         area_seccion = col_double(),
                         inclinacion_peligrosa = col_integer()))


data_test <- read_csv("Universidad/2022 2ndo semestre/Inteligencia artificial/tp7-ml/arbolado mdz/arbolado-mza-dataset-test.csv/arbolado-mza-dataset-test.csv",
                      col_types = cols(
                        id = col_integer(),
                        especie = col_character(),
                        ultima_modificacion = col_character(),
                        altura = col_factor(),
                        circ_tronco_cm = col_double(),
                        diametro_tronco = col_factor(),
                        long = col_double(),
                        lat = col_double(),
                        seccion = col_integer(),
                        nombre_seccion = col_character(),
                        area_seccion = col_double()))

data_train <- data_train %>%
  mutate(inclinacion_peligrosa=ifelse(inclinacion_peligrosa=='1','si','no'))
data_train$inclinacion_peligrosa <- as.factor(data_train$inclinacion_peligrosa)

str(data_train)
View(data_train)
str(data_test)
View(data_test)


model <- randomForest(inclinacion_peligrosa ~ ., data = data_train, mtry=1, ntree=250)

oob.error.data <- data.frame(
  Trees=rep(1:nrow(model$err.rate), times=3),
  Type=rep(c("OOB", "si", "no"), each=nrow(model$err.rate)),
  Error=c(model$err.rate[,"OOB"], 
          model$err.rate[,"si"], 
          model$err.rate[,"no"]))

ggplot(data=oob.error.data, aes(x=Trees, y=Error)) +
  geom_line(aes(color=Type))

preds_tree_probs=predict(model,data_test,type='prob')
head(preds_tree_probs)
View(preds_tree_probs)

preds_tree=ifelse(preds_tree_probs[,2] >=0.010,1,0)
head(preds_tree)

submission<-data.frame(id=data_test$id,inclinacion_peligrosa=preds_tree)
readr::write_csv(submission,"C:\\Users\\Lucas Estudio\\Documents\\Universidad\\2022 2ndo semestre\\Inteligencia artificial\\tp7-ml\\arbolado-mza-dataset-envio4.csv")
View(submission)
