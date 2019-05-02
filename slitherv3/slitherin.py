import argparse
import random
from game.helpers.constants import Constants
from game.models.general_purpose.human_solver import HumanSolver

from game.models.domain_specific.dnn_genetic_evolution_ai_solver import DNNGeneticEvolutionSolver, DNNGeneticEvolutionTrainer
from game.models.general_purpose.ddqn_ai_solver import DDQNSolver, DDQNTrainer


solvers = [
           HumanSolver(),
           DNNGeneticEvolutionSolver(),
           DDQNSolver()
           ]

trainers = [
            DNNGeneticEvolutionTrainer(),
            DDQNTrainer()
            ]

game_models = solvers + trainers


def args():
    parser = argparse.ArgumentParser()
    for game_model in game_models:
        parser.add_argument("-"+game_model.abbreviation, "--"+game_model.short_name,
                            help=game_model.long_name,
                            action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    selected_game_model = random.choice(solvers)
    args = args()
    for game_model in game_models:
        if game_model.short_name in args and vars(args)[game_model.short_name]:
            selected_game_model = game_model
    if selected_game_model in trainers:
        selected_game_model.move(selected_game_model.prepare_training_environment())
    else:
        from game.game import Game
        Game(game_model=selected_game_model,
            fps=Constants.FPS,
            pixel_size=Constants.PIXEL_SIZE,
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT+Constants.NAVIGATION_BAR_HEIGHT,
            navigation_bar_height=int(Constants.NAVIGATION_BAR_HEIGHT))
