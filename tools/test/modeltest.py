from keras.models import load_model
saved_model = load_model('../../models/LoraxV1.0.h5')
import random as rand


# month, day, temp, rh, wind, rain
new_data = [5, 3, 28, 20, 2, 0]
predictions = saved_model.predict([new_data])
print(predictions)

new_data = [(rand.randint(1,12), rand.randint(1,7), rand.randint(20,40), rand.randint(0,100), rand.randint(0,5), rand.randint(0,10)) for i in range(100)]
predictions = saved_model.predict(new_data)
for i in range(len(new_data)):
 print(f"month: {new_data[i][0]} day: {new_data[i][1]} temp: {new_data[i][2]} RH: {new_data[i][3]} wind: {new_data[i][4]} rain: {new_data[i][5]}\nchance of forest fire: {1 - predictions[i][0]:3f}\n")
