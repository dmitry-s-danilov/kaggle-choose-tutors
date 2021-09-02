columns = dict(
    id='Id',
    feature=[
        'age',
        'years_of_experience',
        'lesson_price',
        'qualification',
        'physics',
        'chemistry',
        'biology',
        'english',
        'geography',
        'history',
        'mean_exam_points',
    ],
    target='choose',
)

general_load_params = dict(
    sep=',',
    header=0,
    index_col=columns['id'],
)

specific_load_params = dict(
    train=dict(
        names=[columns['id']] + columns['feature'] + [columns['target']],
    ),
    test=dict(
        names=[columns['id']] + columns['feature'],
    ),
    submission=dict(
        names=[columns['id'], columns['target']],
    )
)

load_params = {
    key: general_load_params | params
    for key, params in specific_load_params.items()
}
