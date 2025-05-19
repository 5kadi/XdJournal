

export const upperPopupState = createPopupState(undefined)

function createPopupState(initialMessage: string | undefined) {
    let message = $state(initialMessage)
    return {
        get message() {return message},
        set message(newMessage) {message = newMessage}
    }
}