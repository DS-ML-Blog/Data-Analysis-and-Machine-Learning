import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def predictions(X, y, tytul, nr):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,
                                                        random_state=1)
    lm = LinearRegression()
    lm.fit(X_train, y_train)

    plt.style.use("classic")

    y_predictions = lm.predict(X_test)

    fig = plt.figure()
    plt.scatter(y_predictions, y_test)
    plt.plot([-20, 40], [-20, 40], "r")
    plt.title("Wartości rzeczywiste vs. Przewidywania \n - "+tytul,
              fontsize=20)
    plt.xlabel("Przewidywania", fontsize=14)
    plt.ylabel("Wartości rzeczywiste", fontsize=14)
    plt.xlim(-30, 50)
    plt.ylim(-40, 50)
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.85,
                        wspace=0.4, hspace=0.35)
    plt.savefig(Figure=fig, fname="plots/2AD"+str(nr)+".png")
    plt.close()

    return y_predictions, y_test
