from keras.models import load_model
saved_model = load_model('../../models/LoraxV1.0.h5')
import random as rand
# new_data = [(rand.randint(1,12), rand.randint(1,7), rand.randint(0,40), rand.randint(0,100), rand.randint(0,10), rand.randint(0,10)) for i in range(100)]

# month, day, temp, rh, wind, rain
new_data = [5, 3, 28, 20, 2, 0]
predictions = saved_model.predict([new_data])
print(predictions)


# predictions = saved_model.predict(new_data)
# for i in range(len(new_data)):
#     print(f"month: {new_data[i][0]} temp: {new_data[i][1]} RH: {new_data[i][2]} wind: {new_data[i][3]} rain: {new_data[i][4]}\nchance of forest fire: {1 - predictions[i][0]:3f}\n")
