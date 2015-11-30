#include "mainwindow.h"
#include "gamegui.h"

#include <QMenuBar>
#include <QMenu>
#include <QAction>

MainWindow::MainWindow()
{
    auto menu = menuBar()->addMenu(tr("Game"));
    auto game3 = menu->addAction(tr("3x3"));
    auto game4 = menu->addAction(tr("4x4"));

    connect(game3, &QAction::triggered, [=]{ new_game(3, 3); });
    connect(game4, &QAction::triggered, [=]{ new_game(4, 4); });

    setWindowTitle(tr("Fifteen Puzzle"));

    new_game(4, 4);
}

void MainWindow::new_game(int cols, int rows)
{
    if (puzzle_ != nullptr) delete puzzle_;
    if (centralWidget() != nullptr) delete centralWidget();

    puzzle_ = new Fifteen{cols, rows};
    setCentralWidget(new GameGui(puzzle_));
    adjustSize();
}

