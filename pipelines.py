from nodes import make_predictions, report_accuracy, split_data, project_data

from project_pipelines import create_pipeline, Node

p = create_pipeline([
    Node(
        make_predictions, 
        ["example_iris_data", "parameters"], 
        ["X_train", "X_test", "y_train", "y_test"], 
        "make_predictions"),
    Node(
        report_accuracy, 
        ["X_train", "X_test", "y_train"], 
        ["y_pred"], 
        "report_accuracy"),
    Node(
        split_data, 
        ["y_pred", "y_test"], 
        None, 
        "split_data"),
    Node(
        project_data, 
        ["y_pred", "y_test"], 
        None, 
        "project_data")
])

deps = p.node_dependencies()

print(deps)