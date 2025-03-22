export default function setGlobalCounter(value: number = 0) {
    let counter = $state(value)

    $effect.root(
        () => {
            $effect(
                () => {
                    console.log('data retrieved')
                    const cachedCounter = localStorage.getItem('counter')
                    if (cachedCounter) counter = JSON.parse(cachedCounter)
                }
            )
            $effect(
                () => {
                    console.log('data set')
                    localStorage.setItem('counter', JSON.stringify(counter))
                }
            )
        }
    )

    return {
        get counter() {
            return counter
        },
        set counter(value: number) {
            counter = value
        }
    }
}