import json
import pandas as pd
import sklearn.metrics as metrics
import seaborn as sn
import matplotlib.pyplot as plt

plots_folder = 'plots'


class Drawing:
    @staticmethod
    def draw_plots(file_name):
        f = open(file_name, 'r')
        df = pd.DataFrame.from_records(json.loads(f.read()))
        f.close()

        paths_to_plots = []

        y_true = df.get('gt_corners')
        labels = list(set(y_true.array))
        labels.sort()
        y_pred = df.get('rb_corners')

        plt.figure()
        confusion_matrix = metrics.confusion_matrix(y_true, y_pred, labels=labels)
        sn.heatmap(confusion_matrix, annot=True, cmap='Blues', fmt='g', xticklabels=labels, yticklabels=labels)
        plt.title('Confusion Matrix')
        plt.xlabel('Predicted')
        plt.ylabel('Ground truth')
        confusion_matrix_name = 'confusion_matrix.png'
        plt.savefig(plots_folder + '/' + confusion_matrix_name)
        paths_to_plots.append(plots_folder + '/' + confusion_matrix_name)

        plt.figure()
        for i in range(0, len(labels)):
            df_filtered = df[df['gt_corners'] == labels[i]]
            plt.scatter(df_filtered.get('floor_mean'), df_filtered.get('ceiling_mean'))
        plt.xlabel('Floor Mean (degrees)')
        plt.ylabel('Ceiling Mean (degrees)')
        plt.legend([f'{i} corners' for i in labels])
        scatter_name = 'scatter.png'
        plt.savefig(plots_folder + '/' + scatter_name)
        paths_to_plots.append(plots_folder + '/' + scatter_name)

        return paths_to_plots

