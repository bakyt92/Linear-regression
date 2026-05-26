import sys

class Training:
    epochs = 100
    learning_rate = 0.01

    def __init__(self):
        self.theta0 = 0
        self.theta1 = 0

    def ft_training(self, headers, data):
        learn_step = 0
        while learn_step < Training.epochs:
            self.ft_iteration(headers, data)
            learn_step += 1
            print(f"Learning: Step # {learn_step}; theta0 = {self.theta0}; theta1 = {self.theta1}.")
        with open("result.csv", "w") as file:
            file.write("theta0, theta1")
            file.write(str(self.theta0) + ", " + str(self.theta1))

    def ft_iteration(self, headers, data):
        price_index = headers.index('price')
        km_index = headers.index('km')
        error_all = []
        error_all_mileage = []
        for x in data:
            estimated_price = self.theta0 + self.theta1 * x[km_index]
            actual_price = x[price_index]
            error_step = estimated_price - actual_price
            error_all.append(float(error_step))
            error_all_mileage.append(float(error_step * x[km_index] / 1000))
        gradient_theta0 = sum(error_all) / len(error_all)
        gradient_theta1 = sum(error_all_mileage) / len(error_all_mileage)
        tmp_theta0 = self.theta0 - (Training.learning_rate * gradient_theta0)
        tmp_theta1 = self.theta1 - (Training.learning_rate * gradient_theta1)
        self.theta0 = tmp_theta0
        self.theta1 = tmp_theta1
        return

