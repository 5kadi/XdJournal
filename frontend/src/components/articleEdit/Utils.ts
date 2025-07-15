import { tick } from "svelte"

function mergeSpanCondition(mainSpan: HTMLSpanElement, compElement: any) {
    const instanceCondition = compElement instanceof HTMLSpanElement 
    if (!instanceCondition) return false //optimized

    let classCondition = true //ensures that merge with different span won't happen
    for (const cssClass of mainSpan.classList) {
        classCondition = classCondition && compElement.classList.contains(cssClass)
    }

    return instanceCondition && classCondition
}

//did it myself yay
function mergeSpansHorizontally(span: HTMLSpanElement) {
    let prev: any = span.previousSibling //ts compiler doesnt understand that if condition is true, then prev is HTMLSpanElement lmao
    let next: any = span.nextSibling

    const prevCondition = mergeSpanCondition(span, prev)
    const nextCondition = mergeSpanCondition(span, next)

    if (!prevCondition && !nextCondition) return 

    if (prevCondition) {
        prev.innerText = prev.innerText + span.innerText
        span.remove()
        span = prev
    }
    if (nextCondition) {
        next.innerText = span.innerText + next.innerText //order is important
        span.remove()
        span = next
    }

    mergeSpansHorizontally(span)
}

function mergeSpanClasses(fragment: DocumentFragment) { //welp, yeah
    return
}


export function wrapContent(selection: Selection, cssClass: string) {
    const range = selection.getRangeAt(0)
    const { textContent } = range.extractContents()

    let span = document.createElement('span')
    span.classList.add(cssClass)
    span.innerText = textContent!

    range.insertNode(span)

    mergeSpansHorizontally(span)

}

/*
export function normalizeContent(selection: Selection) { //doesn't work anyways lmao
    const range = selection.getRangeAt(0)
    const { textContent } = range.extractContents()
    if (!textContent) return

    let normalizedText = document.createEle

    range.insertNode(normalizedText)
} 
*/

export async function caretSpanEscape(selection: Selection, parentDiv: HTMLDivElement) {
    parentDiv.innerHTML += '&nbsp;' //цыганские фокусы
    await tick() //make sure that DOM changes are applied

    const {lastChild} = parentDiv

    let range = document.createRange()
    range.setStart(lastChild!, 1)
    range.setEnd(lastChild!, 1)

    selection.removeAllRanges()
    selection.addRange(range)
}



