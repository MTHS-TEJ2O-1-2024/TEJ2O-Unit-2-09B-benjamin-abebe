/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Mr. Coxall
 * Created on: Sep 2020
 * This program ...
*/

let randomNumber: number = 0
let score: number = 0

score = 0
randomNumber = -1
basic.clearScreen()
basic.showIcon(IconNames.Happy)

input.onGesture(Gesture.Shake, function () {
    randomNumber = randint(0, 2)

    // setting if statement for Rock
    if (randomNumber == 0) {
        basic.showIcon(IconNames.SmallSquare)
        pause(3000)
        basic.showIcon(IconNames.Happy)
    }
    if (randomNumber == 1) {
        basic.showIcon(IconNames.Square)
        pause(3000)
        basic.showIcon(IconNames.Happy)
    }

    if (randomNumber == 2) {
        basic.showIcon(IconNames.Scissors)
        pause(3000)
        basic.showIcon(IconNames.Happy)
    }
})

input.onButtonPressed(Button.A, function() {
    score = score + 1
    basic.showIcon(IconNames.Yes)
    basic.showIcon(IconNames.Happy)
})

input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showString("Score: " + score)
})